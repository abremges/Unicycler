
#ifndef RANDOM_ALIGNMENTS_H
#define RANDOM_ALIGNMENTS_H

#include <seqan/sequence.h>
#include <string>
#include <vector>
#include "scoredalignment.h"
#include <mutex>

using namespace seqan;

// Functions that are called by the Python script must have C linkage, not C++ linkage.
extern "C" {

    char * getRandomSequenceAlignmentScores(int seqLength, int n,
                                            int matchScore, int mismatchScore, int gapOpenScore, int gapExtensionScore);
    char * getRandomSequenceAlignmentErrorRates(int seqLength, int n,
                                               int matchScore, int mismatchScore, int gapOpenScore, int gapExtensionScore);
    char * simulateDepths(int alignmentLengths[], int alignmentCount, int refLength, int iterations, int threadCount);
}

void simulateDepthsOneThread(int alignmentLengths[], int alignmentCount, int refLength, int iterations,
                             std::vector<int> * minDepthCounts, std::vector<int> * maxDepthCounts,
                             std::mutex * mut);

std::string getRandomSequence(int seqLength, std::mt19937 & gen, std::uniform_int_distribution<int> & dist);

char getRandomBase(std::mt19937 & gen, std::uniform_int_distribution<int> & dist);

void getMeanAndStDev(std::vector<double> & v, double & mean, double & stdev);

std::string toStringWithPrecision(double val, int precision);


#endif // RANDOM_ALIGNMENTS_H
