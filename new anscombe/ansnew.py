import pandas as pd
import matplotlib.pyplot as plt
import os
from input_data import x, y1, y2, y3, x4, y4, df_dict


def create_dataframe(df_dict):
    anscombe_df = pd.DataFrame(df_dict, index=x)
    return anscombe_df


def create_directory():
    return os.makedirs('results', exist_ok=True)


def calculations(anscombe_df):
    results = {'mean': [anscombe_df.mean()],
           'correlation': [anscombe_df.reset_index().corr()],
           'standard deviation': [anscombe_df.std(ddof=0)],
           'variation': [anscombe_df.var()]}
    return results


def results_to_csv(results):
    return pd.DataFrame(results)


def saving_results_to_csv(csv_results):
    return csv_results.to_csv(f'results/numeral_results.csv', index=False, header=True, sep=',')


def plot(anscombe_df):
    scatter_plot_df = anscombe_df.reset_index()
    return scatter_plot_df


fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6))
fig.suptitle('Anscombe quartet results', fontsize=16)
for i, ax in enumerate(axs.flat):
    ax.set_title(f'Plot number {i+1}')
plt.setp(axs[-1, :], xlabel='x axis')
plt.setp(axs[:, 0], ylabel='y axis')

axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(0, 4, 8, 12))
axs[0, 0].scatter(x, y1)
axs[0, 1].scatter(x, y2)
axs[1, 0].scatter(x, y3)
axs[1, 1].scatter(x4, y4)

def save_plot():
    return plt.savefig(f'results/charts.png')


def main():
    anscombe_df = create_dataframe(df_dict)
    create_directory()
    results = calculations(anscombe_df)
    csv_results = results_to_csv(results)
    saving_results_to_csv(csv_results)
    plot(anscombe_df)

if __name__ == '__main__':
    main()
