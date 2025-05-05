from mrjob.job import MRJob

class MRCharCount(MRJob):
    def mapper(self, _, line):
        for char in line.strip():
            yield char.lower(), 1
    def reducer(self, char, counts):
        yield char, sum(counts)

if __name__ == '__main__':
    MRCharCount.run()

## sent count

# from mrjob.job import MRJob
# import re

# regex = re.compile(r'[^.!?]*[.!?]')

# class MRSentCount(MRJob):
#     def mapper(self,_,lines):
#         for _ in regex.findall(lines):
#             yield "Sentence(s)", 1
#     def reducer(self, sent, counts):
#         yield sent, sum(counts)

# if __name__ == "__main__":
#     MRSentCount.run()