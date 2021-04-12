import pandas as pd
import matplotlib.pyplot as plt

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

df_dict = {
    'I': y1,
    'II': y2,
    'III': y3,
    'IV': y4
}

anscombe_df = pd.DataFrame(df_dict, index=x)

print(anscombe_df.mean().round(2))
print(anscombe_df.std(ddof=0).round(2))
print(anscombe_df.reset_index().corr().round(2))
print(anscombe_df.var().round(1))

scatter_plot_df = anscombe_df.reset_index()

fig, axs = plt.subplots(2,2, sharex=True, sharey=True, figsize=(6, 6))

axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(0, 4, 8, 12))

axs[0, 0].scatter(x, y1)
axs[0, 1].scatter(x, y2)
axs[1, 0].scatter(x, y3)
axs[1, 1].scatter(x4, y4)

plt.show()
script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Results/')
sample_file_name = "sample"

if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

plt.savefig( results_dir, 'quartet.png')
