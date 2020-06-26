#!/usr/bin/env python3

from collections import defaultdict
import datetime
import gzip
import itertools
import json
import locale


# The current version can be found at http://oeis.org/stripped.gz (CC-BY-NC 3.0)
FILENAME = '/tmp/stripped.gz'
# How many uninteresting number would you like to know?
MAX_UNINTERESTING = 20
# Do you want to graph 'em?
WRITE_COUNTS = False


class Record:
    def __init__(self):
        self.first_a_number = None
        self.occurrence_count = 0

    def merge(self, other):
        self.occurrence_count += other.occurrence_count
        assert other.first_a_number
        if not self.first_a_number:
            self.first_a_number = other.first_a_number

    @staticmethod
    def within(a_number):
        r = Record()
        r.first_a_number = a_number
        r.occurrence_count = 1
        return r


def read_from(filename):
    records = defaultdict(Record)
    total = 0
    last_a = None
    last_modified = 'unknown'
    least_det = (999, None)
    most_det = (0, None)
    for lineno, line in enumerate(gzip.open(filename)):
        if (lineno + 1) % 10000 == 0:
            print('line {}...'.format(lineno + 1))
        if line.startswith(b'# Last Modified: '):
            last_modified = line[len(b'# Last Modified: '):].decode().strip()
            continue
        if line.startswith(b'#'):
            continue
        parts = line.split(b',')
        assert parts[-1] == b'\n', (parts, line, lineno)
        assert parts[0].startswith(b'A'), (parts, line, lineno)
        a_number = parts[0].decode().strip()
        last_a = a_number
        for number in parts[1:-1]:
            number = int(number)
            total += 1
            records[number].merge(Record.within(a_number))
        entries = len(parts) - 2
        if entries < least_det[0]:
            least_det = (entries, a_number)
        if entries > most_det[0]:
            most_det = (entries, a_number)
    last_poll = datetime.datetime.now().astimezone(datetime.timezone.utc)
    return dict(
        last_a=last_a,
        last_modified=last_modified,
        least_det=least_det,
        most_det=most_det,
        records=dict(records),
        last_poll = last_poll.strftime('%B %d %H:%M %Z %Y'),  # e.g. June 26 00:45 UTC 2020
    )


def refine(results):
    records = results['records']

    uninteresting = []
    results['uninteresting'] = uninteresting
    for i in itertools.count():
        if i in records:
            # The number `i` occurs in OEIS, there we consider it "interesting".
            continue
        uninteresting.append(i)
        if len(uninteresting) >= MAX_UNINTERESTING:
            # Should never be greater, but whatever.
            break

    uninteresting_neg = []
    results['uninteresting_neg'] = uninteresting_neg
    for i in itertools.count():
        i = -i
        if i in records:
            # The number `i` occurs in OEIS, there we consider it "interesting".
            continue
        uninteresting_neg.append(i)
        if len(uninteresting_neg) >= MAX_UNINTERESTING:
            # Should never be greater, but whatever.
            break

    results['most_interesting'] = max((r.occurrence_count, n, r.first_a_number) for n, r in records.items())
    results['last_novel'] = max((r.first_a_number, n, r.occurrence_count) for n, r in records.items())
    results['largest'] = max((n, r.first_a_number, r.occurrence_count) for n, r in records.items())
    results['lowest'] = min((n, r.first_a_number, r.occurrence_count) for n, r in records.items())


def printablify(results):
    results['uninteresting_1'] = results['uninteresting'][0]
    results['uninteresting_list'] = ', '.join(str(e) for e in results['uninteresting'][:-1]) + ' and ' + str(results['uninteresting'][-1])
    results['uninteresting_neg_1'] = results['uninteresting_neg'][0]
    results['uninteresting_neg_list'] = ', '.join(str(e) for e in results['uninteresting_neg'][:-1]) + ' and ' + str(results['uninteresting_neg'][-1])
    results['most_det_n'], results['most_det_a'] = results['most_det']
    results['least_det_n'], results['least_det_a'] = results['least_det']
    results['lowest_t'], results['lowest_a'], _ = results['lowest']
    results['largest_t'], results['largest_a'], _ = results['largest']
    results['most_interesting_n'], results['most_interesting_t'], _ = results['most_interesting']
    results['last_novel_a'], results['last_novel_t'], _ = results['last_novel']


def run(filename):
    locale.setlocale(locale.LC_ALL, 'C')
    results = read_from(filename)
    refine(results)
    printablify(results)
    if WRITE_COUNTS:
        with open('results.txt', 'w') as fp:
            for n in range(results['uninteresting_neg'][0] + 1, results['uninteresting'][0]):
                r = results['records'][n]
                fp.write('{}\t{}\t{}\n'.format(n, r.occurrence_count, r.first_a_number.strip('A0')))
        results['records'] = '[SNIP, see file results.txt]'  # Too large to display
    else:
        results['records'] = '[SNIP, too big]'  # Too large to display
    for k, v in results.items():
        print('{}: {}'.format(k, v))
    with open('template.html', 'r') as fp:
        template = fp.read()
    html = template.format(**results)
    with open('gh-pages/index.html', 'w') as fp:
        fp.write(html)
    with open('gh-pages/raw.json', 'w') as fp:
        json.dump(results, fp, indent=1, sort_keys=True)


if __name__ == '__main__':
    run(FILENAME)
