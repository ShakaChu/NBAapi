# %%
import requests
import pandas as pd


def shotchartdetail(leagueid='00', season='2019-20', seasontype='Regular Season', teamid=0,
                    playerid=0, gameid='', outcome='', location='', month=0,
                    seasonseg='', datefrom='', dateto='', oppteamid=0, vsconf='',
                    vsdiv='', pos='', gameseg='', per=0, lastngames=0, aheadbehind='',
                    contextmeasure='FGA', clutchtime='', rookieyear=''):
    '''
    Access to NBA API - http://stats.nba.com/stats/shotchartdetail
    Returns the shotchart requested and the leagueaverage
    Example:
    shot_data,leagueaverage = shotchartdetail(season='2016-17')
    '''
    url = 'https://stats.nba.com/stats/shotchartdetail?'
    api_param = {
        'LeagueID': leagueid,
        'Season': season,
        'SeasonType': seasontype,
        'TeamID': teamid,
        'PlayerID': playerid,
        'GameID': gameid,
        'Outcome': outcome,
        'Location': location,
        'Month': month,
        'SeasonSegment': seasonseg,
        'DateFrom': datefrom,
        'DateTo': dateto,
        'OpponentTeamID': oppteamid,
        'VsConference': vsconf,
        'VsDivision': vsdiv,
        'PlayerPosition': pos,
        'GameSegment': gameseg,
        'Period': per,
        'LastNGames': lastngames,
        'AheadBehind': aheadbehind,
        'ContextMeasure': contextmeasure,
        'ClutchTime': clutchtime,
        'RookieYear': rookieyear,
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url, params=api_param, headers={
        "USER-AGENT": u_a,
        "Referer": "https://stats.nba.com/events/"
    })
    data = response.json()
    shot_chart_detail = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
    league_average = pd.DataFrame(data['resultSets'][1]['rowSet'], columns=data['resultSets'][1]['headers'])
    return shot_chart_detail, league_average