from matplotlib.colors import ListedColormap

vaporwave_colors_ = [
    (0.153, 0.008127, 0.3962), (0.1567, 0.01102, 0.4001),
    (0.1604, 0.01396, 0.4041), (0.1642, 0.01694, 0.4081),
    (0.168, 0.01996, 0.412),   (0.1717, 0.02302, 0.416),
    (0.1755, 0.02613, 0.42),   (0.1793, 0.02928, 0.424),
    (0.1831, 0.03248, 0.428),  (0.1869, 0.03572, 0.432),
    (0.1907, 0.03901, 0.436),  (0.1946, 0.04229, 0.44),
    (0.1984, 0.04546, 0.444),  (0.2022, 0.04853, 0.448),
    (0.2061, 0.05152, 0.4521), (0.2099, 0.05444, 0.4561),
    (0.2138, 0.05729, 0.4601), (0.2176, 0.06008, 0.4641),
    (0.2215, 0.06281, 0.4682), (0.2254, 0.06549, 0.4722),
    (0.2293, 0.06813, 0.4762), (0.2331, 0.07072, 0.4803),
    (0.237, 0.07328, 0.4843),  (0.2409, 0.0758, 0.4883),
    (0.2448, 0.07828, 0.4924), (0.2487, 0.08073, 0.4964),
    (0.2526, 0.08315, 0.5004), (0.2565, 0.08555, 0.5045),
    (0.2604, 0.08791, 0.5085), (0.2643, 0.09026, 0.5126),
    (0.2682, 0.09258, 0.5166), (0.2721, 0.09488, 0.5206),
    (0.276, 0.09716, 0.5247),  (0.2799, 0.09942, 0.5287),
    (0.2839, 0.1017, 0.5328),  (0.2878, 0.1039, 0.5368),
    (0.2917, 0.1061, 0.5409),  (0.2956, 0.1083, 0.5449),
    (0.2996, 0.1105, 0.549),   (0.3035, 0.1126, 0.553),
    (0.3074, 0.1148, 0.557),   (0.3114, 0.1169, 0.5611),
    (0.3153, 0.1191, 0.5651),  (0.3193, 0.1212, 0.5692),
    (0.3232, 0.1233, 0.5732),  (0.3272, 0.1254, 0.5773),
    (0.3311, 0.1275, 0.5813),  (0.3351, 0.1296, 0.5854),
    (0.339, 0.1317, 0.5894),   (0.343, 0.1337, 0.5935),
    (0.3469, 0.1358, 0.5975),  (0.3509, 0.1378, 0.6016),
    (0.3549, 0.1399, 0.6056),  (0.3589, 0.1419, 0.6097),
    (0.3628, 0.144, 0.6138),   (0.3668, 0.146, 0.6178),
    (0.3708, 0.148, 0.6219),   (0.3748, 0.15, 0.6259),
    (0.3787, 0.152, 0.63),     (0.3827, 0.1541, 0.6341),
    (0.3867, 0.1561, 0.6381),  (0.3907, 0.1581, 0.6422),
    (0.3947, 0.1601, 0.6462),  (0.3987, 0.1621, 0.6503),
    (0.4027, 0.1641, 0.6544),  (0.4067, 0.166, 0.6585),
    (0.4107, 0.168, 0.6625),   (0.4147, 0.17, 0.6666),
    (0.4187, 0.172, 0.6707),   (0.4227, 0.174, 0.6748),
    (0.4268, 0.176, 0.6788),   (0.4308, 0.1779, 0.6829),
    (0.4348, 0.1799, 0.687),   (0.4388, 0.1819, 0.6911),
    (0.4429, 0.1839, 0.6952),  (0.4469, 0.1858, 0.6993),
    (0.4509, 0.1878, 0.7033),  (0.455, 0.1898, 0.7074),
    (0.459, 0.1918, 0.7115),   (0.4631, 0.1937, 0.7156),
    (0.4671, 0.1957, 0.7197),  (0.4712, 0.1977, 0.7238),
    (0.4752, 0.1996, 0.7279),  (0.4793, 0.2016, 0.732),
    (0.4834, 0.2036, 0.7361),  (0.4874, 0.2056, 0.7403),
    (0.4915, 0.2075, 0.7444),  (0.4956, 0.2095, 0.7485),
    (0.4997, 0.2115, 0.7526),  (0.5037, 0.2135, 0.7567),
    (0.5078, 0.2154, 0.7609),  (0.5119, 0.2174, 0.765),
    (0.516, 0.2194, 0.7691),   (0.5201, 0.2214, 0.7733),
    (0.5242, 0.2234, 0.7774),  (0.5283, 0.2254, 0.7815),
    (0.5324, 0.2273, 0.7857),  (0.5366, 0.2293, 0.7898),
    (0.5407, 0.2313, 0.794),   (0.5448, 0.2333, 0.7981),
    (0.5489, 0.2353, 0.8023),  (0.5531, 0.2373, 0.8064),
    (0.5572, 0.2393, 0.8106),  (0.5613, 0.2413, 0.8148),
    (0.5655, 0.2433, 0.819),   (0.5696, 0.2453, 0.8231),
    (0.5738, 0.2473, 0.8273),  (0.578, 0.2493, 0.8315),
    (0.5821, 0.2514, 0.8357),  (0.5863, 0.2534, 0.8399),
    (0.5905, 0.2554, 0.8441),  (0.5947, 0.2574, 0.8483),
    (0.5988, 0.2595, 0.8525),  (0.603, 0.2615, 0.8567),
    (0.6072, 0.2635, 0.8609),  (0.6114, 0.2656, 0.8651),
    (0.6156, 0.2676, 0.8693),  (0.6198, 0.2696, 0.8735),
    (0.6241, 0.2717, 0.8778),  (0.6283, 0.2737, 0.882),
    (0.6325, 0.2758, 0.8862),  (0.6367, 0.2779, 0.8905),
    (0.641, 0.2799, 0.8947),   (0.6452, 0.282, 0.899),
    (0.6495, 0.2841, 0.9032),  (0.6537, 0.2861, 0.9075),
    (0.658, 0.2882, 0.9118),   (0.6622, 0.2903, 0.916),
    (0.665, 0.2944, 0.9194),   (0.6663, 0.3004, 0.9218),
    (0.6675, 0.3063, 0.9243),  (0.6687, 0.3122, 0.9267),
    (0.6699, 0.3182, 0.929),   (0.671, 0.324, 0.9314),
    (0.6722, 0.3299, 0.9337),  (0.6732, 0.3357, 0.936),
    (0.6743, 0.3416, 0.9383),  (0.6753, 0.3474, 0.9406),
    (0.6763, 0.3532, 0.9428),  (0.6773, 0.3589, 0.945),
    (0.6782, 0.3647, 0.9472),  (0.6792, 0.3704, 0.9494),
    (0.6801, 0.3762, 0.9515),  (0.6809, 0.3819, 0.9536),
    (0.6817, 0.3876, 0.9557),  (0.6826, 0.3933, 0.9578),
    (0.6833, 0.3989, 0.9598),  (0.6841, 0.4046, 0.9619),
    (0.6848, 0.4102, 0.9639),  (0.6855, 0.4159, 0.9658),
    (0.6862, 0.4215, 0.9678),  (0.6869, 0.4272, 0.9697),
    (0.6875, 0.4328, 0.9716),  (0.6881, 0.4384, 0.9735),
    (0.6887, 0.444, 0.9753),   (0.6892, 0.4496, 0.9772),
    (0.6897, 0.4551, 0.979),   (0.6903, 0.4607, 0.9808),
    (0.6907, 0.4663, 0.9825),  (0.6912, 0.4718, 0.9843),
    (0.6917, 0.4774, 0.986),   (0.6921, 0.4829, 0.9877),
    (0.6925, 0.4885, 0.9893),  (0.6929, 0.494, 0.991),
    (0.6932, 0.4996, 0.9926),  (0.6936, 0.5051, 0.9942),
    (0.6939, 0.5106, 0.9958),  (0.6942, 0.5161, 0.9974),
    (0.6945, 0.5216, 0.9989),  (0.6948, 0.5271, 1.0),
    (0.695, 0.5326, 1.0),      (0.6952, 0.5381, 1.0),
    (0.6955, 0.5436, 1.0),     (0.6957, 0.549, 1.0),
    (0.6959, 0.5545, 1.0),     (0.696, 0.56, 1.0),
    (0.6962, 0.5655, 1.0),     (0.6963, 0.5709, 1.0),
    (0.6965, 0.5764, 1.0),     (0.6966, 0.5818, 1.0),
    (0.6967, 0.5873, 1.0),     (0.6968, 0.5927, 1.0),
    (0.6969, 0.5982, 1.0),     (0.6969, 0.6036, 1.0),
    (0.697, 0.609, 1.0),       (0.6971, 0.6144, 1.0),
    (0.6971, 0.6199, 1.0),     (0.6971, 0.6253, 1.0),
    (0.6972, 0.6307, 1.0),     (0.6972, 0.6361, 1.0),
    (0.6972, 0.6415, 1.0),     (0.6972, 0.6469, 1.0),
    (0.6972, 0.6523, 1.0),     (0.6971, 0.6577, 1.0),
    (0.6971, 0.6631, 1.0),     (0.6971, 0.6685, 1.0),
    (0.6971, 0.6739, 1.0),     (0.697, 0.6793, 1.0),
    (0.697, 0.6847, 1.0),      (0.6969, 0.6901, 1.0),
    (0.6969, 0.6955, 1.0),     (0.6968, 0.7009, 1.0),
    (0.6968, 0.7063, 1.0),     (0.6967, 0.7116, 1.0),
    (0.6967, 0.717, 1.0),      (0.6966, 0.7224, 1.0),
    (0.6965, 0.7278, 1.0),     (0.6965, 0.7331, 1.0),
    (0.6964, 0.7385, 1.0),     (0.6963, 0.7439, 1.0),
    (0.6963, 0.7493, 1.0),     (0.6962, 0.7546, 1.0),
    (0.6962, 0.76, 1.0),       (0.6961, 0.7654, 1.0),
    (0.696, 0.7708, 1.0),      (0.696, 0.7761, 1.0),
    (0.6959, 0.7815, 1.0),     (0.6959, 0.7869, 1.0),
    (0.6958, 0.7922, 1.0),     (0.6958, 0.7976, 1.0),
    (0.6957, 0.803, 1.0),      (0.6957, 0.8084, 1.0),
    (0.6956, 0.8137, 1.0),     (0.6956, 0.8191, 1.0),
    (0.6956, 0.8245, 1.0),     (0.6956, 0.8299, 1.0),
    (0.6955, 0.8352, 1.0),     (0.6955, 0.8406, 1.0),
    (0.6955, 0.846, 1.0),      (0.6955, 0.8514, 1.0),
    (0.6956, 0.8568, 1.0),     (0.6956, 0.8622, 1.0),
    (0.6956, 0.8675, 1.0),     (0.6956, 0.8729, 1.0),
    (0.6957, 0.8783, 1.0),     (0.6957, 0.8837, 1.0),
    (0.6958, 0.8891, 1.0),     (0.6958, 0.8945, 1.0),
    (0.6959, 0.8999, 1.0),     (0.696, 0.9054, 1.0),
    (0.6961, 0.9108, 1.0),     (0.6962, 0.9162, 1.0),
    (0.6963, 0.9216, 1.0),     (0.6965, 0.927, 1.0),
    (0.6966, 0.9325, 1.0),     (0.6967, 0.9379, 1.0),
    (0.6969, 0.9433, 1.0),     (0.6971, 0.9488, 1.0),
    (0.6973, 0.9542, 1.0),     (0.6975, 0.9597, 1.0),
    (0.6977, 0.9651, 1.0),     (0.6979, 0.9706, 1.0),
    (0.6981, 0.9761, 1.0),     (0.6984, 0.9815, 1.0),
    (0.6986, 0.987, 1.0),      (0.6989, 0.9925, 1.0)
]

vaporwave = ListedColormap(vaporwave_colors_, "vaporwave")
