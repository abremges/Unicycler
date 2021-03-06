"""
Various hard-coded settings for Unicycler.

Author: Ryan Wick
email: rrwick@gmail.com
"""

# Unicycler will only work with read alignments if they are long enough. This values specifies
# the threshold relative to the graph overlap. E.g. if this value is 2 and the graph used was a
# SPAdes 95-mer graph, it would have an overlap of 95 bp and so the minimum used alignment would
# be 190 bp.
MIN_ALIGNMENT_LENGTH_RELATIVE_TO_GRAPH_OVERLAP = 2

# If less than this fraction of a read was aligned in the first aligning pass, Unicycler will try
# again using much more sensitive alignment settings. This helps to align reads which come from
# particularly difficult repetitive regions.
MIN_READ_FRACTION_ALIGNED = 0.9

# This is how much overlap is allowed between two alignments in a single read, relative to the
# graph's overlap. For example, if the graph has an overlap of 95 and this value is 1.1,
# then alignments within a read can go up to 105 bp, but alignments with more overlap will be
# filtered out.
ALLOWED_ALIGNMENT_OVERLAP = 1.1

# Unicycler will not use the lowest quality alignments for making bridges. This setting specifies
# the threshold. E.g. if it is 5, then any alignment with a scaled score of less than the 5th
# percentile scaled score will be thrown out.
MIN_SCALED_SCORE_PERCENTILE = 5.0

# Unicycler-align can automatically determine a low score threshold. It does this by randomly
# aligning 100 bp sequences with the current scoring scheme and determining the mean and standard
# deviation of such random alignments. The threshold is then set to a certain number of standard
# deviations above the mean (this setting). This should ensure that any alignment which passes
# the threshold is at least a little bit better than a random sequence alignment.
AUTO_SCORE_STDEV_ABOVE_RANDOM_ALIGNMENT_MEAN = 5

# When Unicycler is searching for paths connecting two graph segments which matches a read
# consensus sequence, it will only consider paths which have a length similar to the expected
# sequence (based on the consensus sequence length). These settings define the acceptable range.
# E.g. if they are 0.7 and 1.3, Unicycler will consider graph paths that range from 70% to 130%
# of the expected sequence length.
MIN_RELATIVE_PATH_LENGTH = 0.9
MAX_RELATIVE_PATH_LENGTH = 1.1
RELATIVE_PATH_LENGTH_BUFFER_SIZE = 100

# These settings are used when Unicycler is exhaustively searching for paths connecting two graph
# segments. If the number of working paths or the number of final paths gets too high during the
# search (exceeds these thresholds), Unicycler will give up and instead try a progressive path
# search.
ALL_PATH_SEARCH_MAX_WORKING_PATHS = 10000
ALL_PATH_SEARCH_MAX_FINAL_PATHS = 250

# These settings are used when Unicycler is progressively searching for paths connecting two graph
# segments. When its number of working paths reaches PROGRESSIVE_PATH_SEARCH_MAX_WORKING_PATHS, it
# will cull them down by scoring the alignment of each. Paths which have a score within the
# PROGRESSIVE_PATH_SEARCH_SCORE_FRACTION of the best are kept.
PROGRESSIVE_PATH_SEARCH_MAX_WORKING_PATHS = 500
PROGRESSIVE_PATH_SEARCH_SCORE_FRACTION = 0.99

# These settings are used for Unicycler's copy number determination - the process by which it
# tries to figure out the depth of constituent components of each segment.
#   * INITIAL_SINGLE_COPY_TOLERANCE controls how much excess depth is acceptable for the first
#     single-copy assignment pass.
#   * COPY_PROPAGATION_TOLERANCE controls how much discrepancy is allowed when propagating copy
#     depths from one segment to the next.
#   * MIN_SINGLE_COPY_LENGTH is how short of a segment can be called single-copy when adding
#     additional single copy segments.
#   * MIN_HALF_MEDIAN_FOR_DIPLOID is used when determining whether a graph should be considered
#     diploid or not for copy depths. At least this fraction of the bases must be near in depth to
#     half of the graph's median value in order for the single-copy depth to be shifted down to
#     0.5.
#   * MAX_COPY_DEPTH_DISTRIBUTION_ARRANGEMENTS caps the number of possible ways to redistribute a
#     segment's copy depths to its neighbours. If there are more possibilities than this,
#     Unicycler won't bother trying.
INITIAL_SINGLE_COPY_TOLERANCE = 0.1
COPY_PROPAGATION_TOLERANCE = 0.5
MIN_SINGLE_COPY_LENGTH = 1000
MIN_HALF_MEDIAN_FOR_DIPLOID = 0.1
MAX_COPY_DEPTH_DISTRIBUTION_ARRANGEMENTS = 10000

# When Unicycler is cleaning up the graph after bridging, it can delete graph paths and graph
# components which are mostly (but not entirely) used up in bridges. This value controls the
# threshold. Making it smaller will make Unicycler more willing to delete stuff. Making it larger
# will make Unicycler less willing to delete stuff.
CLEANING_USEDUPNESS_THRESHOLD = 0.5

# When making a consensus sequence, Unicycler will use up to this many read sequences. It is
# capped because a consensus with too many reads will take too long and likely not be much
# better. E.g. a 100 read consensus will likely give a similar sequence as a 25 read consensus,
# but it will take much longer.
MAX_READS_FOR_CONSENSUS = 25

# When cleaning a SPADes assembly, Unicycler will delete graph segments will less depth than
# this, if doing so will not break up the graph.
READ_DEPTH_FILTER = 0.5

# The different bridging modes have different minimum bridge quality thresholds.
CONSERVATIVE_MIN_BRIDGE_QUAL = 25.0
NORMAL_MIN_BRIDGE_QUAL = 10.0
BOLD_MIN_BRIDGE_QUAL = 1.0

# These control how often progress lines are updated in the stdout. They define the percentage step
# used. E.g. if set to 5.0, the progress will go 5%, 10%, 15%, etc.
# Setting these to higher values helps to prevent excessive progress updates, which is a pain when
# piping Unicycler output to file.
LOADING_REFERENCES_PROGRESS_STEP = 1.0
LOADING_READS_PROGRESS_STEP = 1.0
LOADING_ALIGNMENTS_PROGRESS_STEP = 1.0
BUILDING_BRIDGES_PROGRESS_STEP = 1.0

# These settings control how willing Unicycler is to make bridges that don't have a graph path.
# This depends on whether one or both of the segments being bridged ends in a dead end and
# whether we have any expected linear sequences (i.e. whether real dead ends are expected).
# If we don't expect any linear sequences, then bridging two dead ends with a pathless bridge is
# great (not at all penalised), bridging a dead end with a non-dead end is okay, and bridging two
# non-dead ends is very much discouraged (quite penalised). If we do expect linear sequences, then
# we are less willing to make bridges between dead ends because it's possible those dead ends are
# genuine and should remain dead ends.
PATHLESS_BRIDGE_QUAL_TWO_DEAD_ENDS = 1.0
PATHLESS_BRIDGE_QUAL_ONE_DEAD_END = 0.7
PATHLESS_BRIDGE_QUAL_NO_DEAD_ENDS = 0.2
PATHLESS_BRIDGE_QUAL_TWO_DEAD_ENDS_WITH_LINEAR_SEQS = 0.6
PATHLESS_BRIDGE_QUAL_ONE_DEAD_END_WITH_LINEAR_SEQS = 0.4
PATHLESS_BRIDGE_QUAL_NO_DEAD_ENDS_WITH_LINEAR_SEQS = 0.2

# If the user doesn't set the thread manually, it will use either the CPU count or this value,
# whichever is smaller. This is to prevent Unicycler from grabbing too many cores by default.
# E.g. if it was run on a large machine with 80 cores, it shouldn't use all 80 unless the user
# explicitly asks for it!
MAX_AUTO_THREAD_COUNT = 8

# The default sequence line wrapping length (e.g. for use in FASTA files).
BASES_PER_FASTA_LINE = 70
