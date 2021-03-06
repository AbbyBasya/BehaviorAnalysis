from .peak_detection import detect_peaks
from .peak_selection import select_peaks
from .peak_localization import localize_peaks
from .motion_estimation import (estimate_motion,
    make_motion_histogram, compute_pairwise_displacement, compute_global_displacement)
from .motion_correction import correct_motion_on_peaks, correct_motion_on_traces
from .template_matching import find_spikes_from_templates, template_matching_methods
from .clustering import find_cluster_from_peaks, clustering_methods

