class Amie():
    def __init__(self):
        self.triples = {}

    def load_checkpoint(self, file):
        with open(file, 'r') as f:
            for line in f.readlines():
                s, p, o, score = line.split(sep='\t')
                s, p, o, score = int(s), int(p), int(o), float(score)

                if p not in self.triples.keys():
                    self.triples[p] = []

                self.triples[p].append((s, o, score))

        for k in self.triples.keys():
            self.triples[p].sort(key=lambda element: (element[1], element[2]))

    def predict(self, batch):
        scores = []
        # Assuming the whole batch contains the same relation.
        r = batch['batch_r'][0].item()

        for i in range(len(batch['batch_h'])):
            h, t = batch['batch_h'][i].item(), batch['batch_t'][i].item()

            found = self.binary_search(r, h, t)
            if found >= 0:
                (h, t, score) = self.triples[r][found]
                scores.append(1.0 - score)
            else:
                scores.append(1.0)

        return scores

    def binary_search(self, p, s, o, lo=0, hi=None):
        if p in self.triples.keys():
            x = (s, o)
            if hi is None:
                hi = len(self.triples[p])
            while lo < hi:
                mid = (lo + hi) // 2
                (ss, oo, score) = self.triples[p][mid]
                midval = (ss, oo)
                if midval < x:
                    lo = mid + 1
                elif midval > x:
                    hi = mid
                else:
                    return mid
        return -1
