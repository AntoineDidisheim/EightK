import didipack as didi
from matplotlib import pyplot as plt
from data import Data
from parameters import *

if __name__ == '__main__':
    args = didi.parse()
    par = Params()
    data = Data(par)
    df = data.load_logs_ev_study()

    ati = data.load_icf_ati_filter()
    ati = ati.rename(columns={'date':'form_date'})
    ati = ati.loc[ati['items'].isin(Constant.LIST_ITEMS_TO_USE),['form_date','form_id','news0','permno']].drop_duplicates()
    df = df.merge(ati)
    df['year'] = df['form_date'].dt.year

    temp = df.loc[:,:].groupby(['dist','permno','news0','year'])['ip'].mean().reset_index()
    temp = temp.pivot(columns='news0',index=['dist','permno','year'],values='ip')
    temp['covered_r'] = temp[1.0]/temp[0.0]
    temp = temp.dropna()
    temp = temp.reset_index()
    temp = temp.merge(data.load_mkt_cap_yearly())
    for d in np.sort(temp['mcap_d'].unique()):
        temp.loc[temp['mcap_d']==d,:].groupby('dist')['covered_r'].median().plot()
        plt.title(f'MCAP d = {d}')
        plt.grid()
        plt.show()

    temp.loc[:, :].groupby('dist')['covered_r'].mean().plot()
    plt.title(f'MCAP all')
    plt.grid()
    plt.show()



    temp.loc[temp['dist']<41, :].groupby('dist')[[0.0,1.0]].median().plot()
    plt.title(f'MCAP all')
    plt.grid()
    plt.show()


    temp = df.loc[:,:].groupby(['dist','permno','news0'])['ip'].mean().reset_index()
    temp = temp.pivot(columns='news0',index=['dist','permno'],values='ip')
    temp['covered_r'] = temp[1.0]/temp[0.0]
    temp = temp.dropna()
    temp = temp.reset_index()

    temp.loc[:, :].groupby('dist')['covered_r'].median().plot()
    plt.title(f'MCAP all')
    plt.grid()
    plt.show()


    df = data.load_logs_ev_study()
    ati = data.load_icf_ati_filter()
    ati = ati.rename(columns={'date':'form_date'})
    ati = ati.loc[ati['items'].isin(Constant.LIST_ITEMS_TO_USE),['form_date','form_id','news0','permno','items']].drop_duplicates()
    df = df.merge(ati)
    cov_per_item = df.groupby(['items','news0'])['ip'].count().reset_index().pivot(columns='news0',index='items',values='ip').fillna(0.0)
    # Your existing data processing code remains the same.

    # Define the subplot grid
    fig, axs = plt.subplots(5, 4, figsize=(20, 25))  # Adjust figsize as needed
    axs = axs.flatten()  # Flatten the axes array for easy indexing

    # Iterate over items and plot
    i = 0
    for _, items in enumerate(np.sort(np.unique(df['items']))):
        if cov_per_item.loc[items, :].min() > 2000:
            temp = df.loc[df['items'] == items, :].groupby(['dist', 'permno', 'news0'])['ip'].mean().reset_index()
            temp = temp.pivot(columns='news0', index=['dist', 'permno'], values='ip')
            temp['covered_r'] = temp[1.0] / temp[0.0]
            temp = temp.dropna()
            temp = temp.reset_index()

            # Plot on the respective subplot
            temp.groupby('dist')['covered_r'].median().plot(ax=axs[i])
            axs[i].set_title(f'Items {items}')
            axs[i].grid()
            i+=1

    # Show the entire grid of plots
    plt.tight_layout()
    plt.show()






