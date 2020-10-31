def data_per_week(df, weeknumber):
    df_week = df.loc[df['week'] == weeknumber]
    
    return df_week


def data_pie_per_match(df_week):
    
    data = df_week.groupby(['matches', 'passResult'])[['passResult']].count()
    data = data.add_suffix('_Count').reset_index()
    pie_data = data.set_index(['matches', 'passResult']).unstack('matches').reset_index()
    pie_data = pie_data.set_index(['passResult'])
    pie_data.columns = pie_data.columns.droplevel(0)
    pie_per_match = pie_data.reset_index()
    
    return pie_per_match

def bar_passRes_match(df, match):
    bar_data = df.groupby(['matches', 'possessionTeam', 'passResult'])[['passResult']].count()
    bar_data = bar_data.add_suffix('_Count').reset_index()
    bar_data_match = bar_data.loc[bar_data['matches']== match]
    bar_data_match = bar_data_match.set_index(['matches', 'passResult', 'possessionTeam']).unstack('matches').reset_index()
    bar_data_match = bar_data_match.set_index(['passResult', 'possessionTeam'])
    bar_data_match.columns = bar_data_match.columns.droplevel(0)
    bar_data_match = bar_data_match.reset_index()
    
    return bar_data_match