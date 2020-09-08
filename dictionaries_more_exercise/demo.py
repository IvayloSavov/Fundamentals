# count_dwarfs_hat_color = {}
#
# for color, dwarfs in all_draws_keys_hat_color.items():
#     count_dwarfs = len(dwarfs.keys())
#     count_dwarfs_hat_color[color] = count_dwarfs
#
# sorted_count_dwarfs_hat_color = dict(sorted(count_dwarfs_hat_color.items(), key=lambda x: -x[1]))
#
# sorted_dwarfs_by_color = {}
# for color in sorted_count_dwarfs_hat_color.keys():
#     dwarfs_in_current_hat_color = all_draws_keys_hat_color[color]
#     sorted_dwarfs = dict(sorted(dwarfs_in_current_hat_color.items(), key=lambda y: -y[1]))
#     sorted_dwarfs_by_color[color] = sorted_dwarfs