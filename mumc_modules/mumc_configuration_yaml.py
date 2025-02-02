#!/usr/bin/env python3
import json
from mumc_modules.mumc_output import save_yaml_config


def filterYAMLConfigKeys(dirty_dict,*clean_keys):

    return {cleanKey:dirty_dict[cleanKey] for cleanKey in clean_keys}


def yaml_configurationBuilder(the_dict):

    #strip out uneccessary data
    config_data=filterYAMLConfigKeys(the_dict,'version','basic_settings','advanced_settings','admin_settings','DEBUG')

    #start building config yaml
    config_data['basic_settings']['filter_statements']['movie']['played']['condition_days']=-1
    config_data['basic_settings']['filter_statements']['movie']['played']['count_equality']='>='
    config_data['basic_settings']['filter_statements']['movie']['played']['count']=1
    config_data['basic_settings']['filter_statements']['movie']['created']['condition_days']=-1
    config_data['basic_settings']['filter_statements']['movie']['created']['count_equality']='>='
    config_data['basic_settings']['filter_statements']['movie']['created']['count']=1
    config_data['basic_settings']['filter_statements']['movie']['created']['behavioral_control']=True

    config_data['basic_settings']['filter_statements']['episode']['played']['condition_days']=-1
    config_data['basic_settings']['filter_statements']['episode']['played']['count_equality']='>='
    config_data['basic_settings']['filter_statements']['episode']['played']['count']=1
    config_data['basic_settings']['filter_statements']['episode']['created']['condition_days']=-1
    config_data['basic_settings']['filter_statements']['episode']['created']['count_equality']='>='
    config_data['basic_settings']['filter_statements']['episode']['created']['count']=1
    config_data['basic_settings']['filter_statements']['episode']['created']['behavioral_control']=True

    config_data['basic_settings']['filter_statements']['audio']['played']['condition_days']=-1
    config_data['basic_settings']['filter_statements']['audio']['played']['count_equality']='>='
    config_data['basic_settings']['filter_statements']['audio']['played']['count']=1
    config_data['basic_settings']['filter_statements']['audio']['created']['condition_days']=-1
    config_data['basic_settings']['filter_statements']['audio']['created']['count_equality']='>='
    config_data['basic_settings']['filter_statements']['audio']['created']['count']=1
    config_data['basic_settings']['filter_statements']['audio']['created']['behavioral_control']=True

    if (config_data['admin_settings']['server']['brand'] == 'jellyfin'):
        config_data['basic_settings']['filter_statements']['audiobook']['played']['condition_days']=-1
        config_data['basic_settings']['filter_statements']['audiobook']['played']['count_equality']='>='
        config_data['basic_settings']['filter_statements']['audiobook']['played']['count']=1
        config_data['basic_settings']['filter_statements']['audiobook']['created']['condition_days']=-1
        config_data['basic_settings']['filter_statements']['audiobook']['created']['count_equality']='>='
        config_data['basic_settings']['filter_statements']['audiobook']['created']['count']=1
        config_data['basic_settings']['filter_statements']['audiobook']['created']['behavioral_control']=True

    config_data['advanced_settings']['filter_statements']['movie']['query_filter']['favorited']=True
    config_data['advanced_settings']['filter_statements']['movie']['query_filter']['whitetagged']=False
    config_data['advanced_settings']['filter_statements']['movie']['query_filter']['blacktagged']=False
    config_data['advanced_settings']['filter_statements']['movie']['query_filter']['whitelisted']=False
    config_data['advanced_settings']['filter_statements']['movie']['query_filter']['blacklisted']=True

    config_data['advanced_settings']['filter_statements']['episode']['query_filter']['favorited']=True
    config_data['advanced_settings']['filter_statements']['episode']['query_filter']['whitetagged']=False
    config_data['advanced_settings']['filter_statements']['episode']['query_filter']['blacktagged']=False
    config_data['advanced_settings']['filter_statements']['episode']['query_filter']['whitelisted']=False
    config_data['advanced_settings']['filter_statements']['episode']['query_filter']['blacklisted']=True

    config_data['advanced_settings']['filter_statements']['audio']['query_filter']['favorited']=True
    config_data['advanced_settings']['filter_statements']['audio']['query_filter']['whitetagged']=False
    config_data['advanced_settings']['filter_statements']['audio']['query_filter']['blacktagged']=False
    config_data['advanced_settings']['filter_statements']['audio']['query_filter']['whitelisted']=False
    config_data['advanced_settings']['filter_statements']['audio']['query_filter']['blacklisted']=True

    if (config_data['admin_settings']['server']['brand'] == 'jellyfin'):
        config_data['advanced_settings']['filter_statements']['audiobook']['query_filter']['favorited']=True
        config_data['advanced_settings']['filter_statements']['audiobook']['query_filter']['whitetagged']=False
        config_data['advanced_settings']['filter_statements']['audiobook']['query_filter']['blacktagged']=False
        config_data['advanced_settings']['filter_statements']['audiobook']['query_filter']['whitelisted']=False
        config_data['advanced_settings']['filter_statements']['audiobook']['query_filter']['blacklisted']=True

    config_data['advanced_settings']['behavioral_statements']['movie']['favorited']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['movie']['favorited']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['movie']['favorited']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['movie']['favorited']['action_control']=3
    config_data['advanced_settings']['behavioral_statements']['movie']['favorited']['extra']['genre']=0
    config_data['advanced_settings']['behavioral_statements']['movie']['favorited']['extra']['library_genre']=0

    config_data['advanced_settings']['behavioral_statements']['movie']['whitetagged']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['movie']['whitetagged']['user_conditional']='all'
    config_data['advanced_settings']['behavioral_statements']['movie']['whitetagged']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['movie']['whitetagged']['action_control']=0

    config_data['advanced_settings']['behavioral_statements']['movie']['blacktagged']['action']='delete'
    config_data['advanced_settings']['behavioral_statements']['movie']['blacktagged']['user_conditional']='all'
    config_data['advanced_settings']['behavioral_statements']['movie']['blacktagged']['played_conditional']='any_played'
    config_data['advanced_settings']['behavioral_statements']['movie']['blacktagged']['action_control']=0

    config_data['advanced_settings']['behavioral_statements']['movie']['whitelisted']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['movie']['whitelisted']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['movie']['whitelisted']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['movie']['whitelisted']['action_control']=3

    config_data['advanced_settings']['behavioral_statements']['movie']['blacklisted']['action']='delete'
    config_data['advanced_settings']['behavioral_statements']['movie']['blacklisted']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['movie']['blacklisted']['played_conditional']='any_played'
    config_data['advanced_settings']['behavioral_statements']['movie']['blacklisted']['action_control']=3
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['action_control']=3
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['extra']['genre']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['extra']['season_genre']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['extra']['series_genre']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['extra']['library_genre']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['extra']['studio_network']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['extra']['studio_network_genre']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['whitetagged']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['episode']['whitetagged']['user_conditional']='all'
    config_data['advanced_settings']['behavioral_statements']['episode']['whitetagged']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['episode']['whitetagged']['action_control']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['blacktagged']['action']='delete'
    config_data['advanced_settings']['behavioral_statements']['episode']['blacktagged']['user_conditional']='all'
    config_data['advanced_settings']['behavioral_statements']['episode']['blacktagged']['played_conditional']='any_played'
    config_data['advanced_settings']['behavioral_statements']['episode']['blacktagged']['action_control']=0
    config_data['advanced_settings']['behavioral_statements']['episode']['whitelisted']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['episode']['whitelisted']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['episode']['whitelisted']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['episode']['whitelisted']['action_control']=3
    config_data['advanced_settings']['behavioral_statements']['episode']['blacklisted']['action']='delete'
    config_data['advanced_settings']['behavioral_statements']['episode']['blacklisted']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['episode']['blacklisted']['played_conditional']='any_played'
    config_data['advanced_settings']['behavioral_statements']['episode']['blacklisted']['action_control']=3
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['action_control']=3
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['extra']['genre']=0
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['extra']['album_genre']=0
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['extra']['library_genre']=0
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['extra']['track_artist']=0
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['extra']['album_artist']=0
    config_data['advanced_settings']['behavioral_statements']['audio']['whitetagged']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['audio']['whitetagged']['user_conditional']='all'
    config_data['advanced_settings']['behavioral_statements']['audio']['whitetagged']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['audio']['whitetagged']['action_control']=0
    config_data['advanced_settings']['behavioral_statements']['audio']['blacktagged']['action']='delete'
    config_data['advanced_settings']['behavioral_statements']['audio']['blacktagged']['user_conditional']='all'
    config_data['advanced_settings']['behavioral_statements']['audio']['blacktagged']['played_conditional']='any_played'
    config_data['advanced_settings']['behavioral_statements']['audio']['blacktagged']['action_control']=0
    config_data['advanced_settings']['behavioral_statements']['audio']['whitelisted']['action']='keep'
    config_data['advanced_settings']['behavioral_statements']['audio']['whitelisted']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['audio']['whitelisted']['played_conditional']='ignore'
    config_data['advanced_settings']['behavioral_statements']['audio']['whitelisted']['action_control']=3
    config_data['advanced_settings']['behavioral_statements']['audio']['blacklisted']['action']='delete'
    config_data['advanced_settings']['behavioral_statements']['audio']['blacklisted']['user_conditional']='any'
    config_data['advanced_settings']['behavioral_statements']['audio']['blacklisted']['played_conditional']='any_played'
    config_data['advanced_settings']['behavioral_statements']['audio']['blacklisted']['action_control']=3
    if (config_data['admin_settings']['server']['brand'] == 'jellyfin'):
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['action']='keep'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['user_conditional']='any'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['played_conditional']='ignore'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['action_control']=3
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['extra']['genre']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['extra']['audiobook_genre']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['extra']['library_genre']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['extra']['track_author']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['extra']['author']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['extra']['library_author']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitetagged']['action']='keep'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitetagged']['user_conditional']='all'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitetagged']['played_conditional']='ignore'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitetagged']['action_control']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacktagged']['action']='delete'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacktagged']['user_conditional']='all'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacktagged']['played_conditional']='any_played'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacktagged']['action_control']=0
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitelisted']['action']='keep'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitelisted']['user_conditional']='any'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitelisted']['played_conditional']='ignore'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['whitelisted']['action_control']=3
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacklisted']['action']='delete'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacklisted']['user_conditional']='any'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacklisted']['played_conditional']='any_played'
        config_data['advanced_settings']['behavioral_statements']['audiobook']['blacklisted']['action_control']=3
    config_data['advanced_settings']['episode_control']['minimum_episodes']=0
    config_data['advanced_settings']['episode_control']['minimum_played_episodes']=0
    config_data['advanced_settings']['episode_control']['minimum_episodes_behavior']='Max Played Min Unplayed'
    config_data['advanced_settings']['trakt_fix']['set_missing_last_played_date']['movie']=True
    config_data['advanced_settings']['trakt_fix']['set_missing_last_played_date']['episode']=True
    config_data['advanced_settings']['trakt_fix']['set_missing_last_played_date']['audio']=True
    if (config_data['admin_settings']['server']['brand'] == 'jellyfin'):
        config_data['advanced_settings']['trakt_fix']['set_missing_last_played_date']['audiobook']=True
    config_data['advanced_settings']['console_controls']['headers']['script']['show']=True
    config_data['advanced_settings']['console_controls']['headers']['script']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['headers']['script']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['headers']['script']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['headers']['user']['show']=True
    config_data['advanced_settings']['console_controls']['headers']['user']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['headers']['user']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['headers']['user']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['headers']['summary']['show']=True
    config_data['advanced_settings']['console_controls']['headers']['summary']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['headers']['summary']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['headers']['summary']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['footers']['script']['show']=True
    config_data['advanced_settings']['console_controls']['footers']['script']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['footers']['script']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['footers']['script']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['warnings']['script']['show']=True
    config_data['advanced_settings']['console_controls']['warnings']['script']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['warnings']['script']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['warnings']['script']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['delete']['show']=True
    config_data['advanced_settings']['console_controls']['movie']['delete']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['delete']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['movie']['delete']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['keep']['show']=True
    config_data['advanced_settings']['console_controls']['movie']['keep']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['keep']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['movie']['keep']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['post_processing']['show']=True
    config_data['advanced_settings']['console_controls']['movie']['post_processing']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['post_processing']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['movie']['post_processing']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['summary']['show']=True
    config_data['advanced_settings']['console_controls']['movie']['summary']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['movie']['summary']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['movie']['summary']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['delete']['show']=True
    config_data['advanced_settings']['console_controls']['episode']['delete']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['delete']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['episode']['delete']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['keep']['show']=True
    config_data['advanced_settings']['console_controls']['episode']['keep']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['keep']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['episode']['keep']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['post_processing']['show']=True
    config_data['advanced_settings']['console_controls']['episode']['post_processing']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['post_processing']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['episode']['post_processing']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['summary']['show']=True
    config_data['advanced_settings']['console_controls']['episode']['summary']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['episode']['summary']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['episode']['summary']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['delete']['show']=True
    config_data['advanced_settings']['console_controls']['audio']['delete']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['delete']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['audio']['delete']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['keep']['show']=True
    config_data['advanced_settings']['console_controls']['audio']['keep']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['keep']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['audio']['keep']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['post_processing']['show']=True
    config_data['advanced_settings']['console_controls']['audio']['post_processing']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['post_processing']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['audio']['post_processing']['formatting']['background']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['summary']['show']=True
    config_data['advanced_settings']['console_controls']['audio']['summary']['formatting']['font']['color']=''
    config_data['advanced_settings']['console_controls']['audio']['summary']['formatting']['font']['style']=''
    config_data['advanced_settings']['console_controls']['audio']['summary']['formatting']['background']['color']=''
    if (config_data['admin_settings']['server']['brand'] == 'jellyfin'):
        config_data['advanced_settings']['console_controls']['audiobook']['delete']['show']=True
        config_data['advanced_settings']['console_controls']['audiobook']['delete']['formatting']['font']['color']=''
        config_data['advanced_settings']['console_controls']['audiobook']['delete']['formatting']['font']['style']=''
        config_data['advanced_settings']['console_controls']['audiobook']['delete']['formatting']['background']['color']=''
        config_data['advanced_settings']['console_controls']['audiobook']['keep']['show']=True
        config_data['advanced_settings']['console_controls']['audiobook']['keep']['formatting']['font']['color']=''
        config_data['advanced_settings']['console_controls']['audiobook']['keep']['formatting']['font']['style']=''
        config_data['advanced_settings']['console_controls']['audiobook']['keep']['formatting']['background']['color']=''
        config_data['advanced_settings']['console_controls']['audiobook']['post_processing']['show']=True
        config_data['advanced_settings']['console_controls']['audiobook']['post_processing']['formatting']['font']['color']=''
        config_data['advanced_settings']['console_controls']['audiobook']['post_processing']['formatting']['font']['style']=''
        config_data['advanced_settings']['console_controls']['audiobook']['post_processing']['formatting']['background']['color']=''
        config_data['advanced_settings']['console_controls']['audiobook']['summary']['show']=True
        config_data['advanced_settings']['console_controls']['audiobook']['summary']['formatting']['font']['color']=''
        config_data['advanced_settings']['console_controls']['audiobook']['summary']['formatting']['font']['style']=''
        config_data['advanced_settings']['console_controls']['audiobook']['summary']['formatting']['background']['color']=''
    config_data['advanced_settings']['UPDATE_CONFIG']=False
    config_data['advanced_settings']['REMOVE_FILES']=False
    config_data['admin_settings']['api_controls']['attempts']=4
    config_data['admin_settings']['api_controls']['item_limit']=25
    config_data['admin_settings']['cache']['size']=32
    config_data['admin_settings']['cache']['fallback_behavior']='LRU'
    config_data['admin_settings']['cache']['minimum_age']=200

    #before saving; reorder some keys for consistency
    config_data['advanced_settings']['behavioral_statements']['movie']['favorited']['extra']=config_data['advanced_settings']['behavioral_statements']['movie']['favorited'].pop('extra')
    config_data['advanced_settings']['behavioral_statements']['episode']['favorited']['extra']=config_data['advanced_settings']['behavioral_statements']['episode']['favorited'].pop('extra')
    config_data['advanced_settings']['behavioral_statements']['audio']['favorited']['extra']=config_data['advanced_settings']['behavioral_statements']['audio']['favorited'].pop('extra')
    if (config_data['admin_settings']['server']['brand'] == 'jellyfin'):
        config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited']['extra']=config_data['advanced_settings']['behavioral_statements']['audiobook']['favorited'].pop('extra')

    #save yaml config file
    save_yaml_config(config_data,str(the_dict['mumc_path']) + '/' + the_dict['config_file_name_yaml'])