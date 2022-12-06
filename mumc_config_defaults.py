#!/usr/bin/env python3

#This module can be used to change some of the default configuration values used before the script is first run
#Script will check for valid values after the first run
#Configuration values outside of the valid range will throw an error
#See https://github.com/terrelsa13/MUMC for a description of each configuration value


defaultConfigValues={

        #'example_number_config':0
        #'example_string_config':'abc'
        #'example_boolean_config':True

        #-------------Basic Config Options Start Here---------------#

        'movie_played_days':-1,
        'movie_created_days':-1,
        
        'episode_played_days':-1,
        'episode_created_days':-1,
        
        'audio_played_days':-1,
        'audio_created_days':-1,
        
        'audiobook_played_days':-1,
        'audiobook_created_days':-1,

        'movie_played_count_comparison':'>=',
        'movie_created_played_count_comparison':'>=',
        
        'episode_played_count_comparison':'>=',
        'episode_created_played_count_comparison':'>=',
        
        'audio_played_count_comparison':'>=',
        'audio_created_played_count_comparison':'>=',
        
        'audiobook_played_count_comparison':'>=',
        'audiobook_created_played_count_comparison':'>=',

        'movie_played_count':1,
        'movie_created_played_count':1,
        
        'episode_played_count':1,
        'episode_created_played_count':1,
        
        'audio_played_count':1,
        'audio_created_played_count':1,
        
        'audiobook_played_count':1,
        'audiobook_created_played_count':1,

        #------------Advanced Config Options Start Here-------------#

        'multiuser_play_count_movie':0,
        'multiuser_play_count_episode':0,
        'multiuser_play_count_audio':0,
        'multiuser_play_count_audiobook':0,

        'keep_favorites_movie':1,
        'keep_favorites_episode':1,
        'keep_favorites_audio':1,
        'keep_favorites_audiobook':1,

        'multiuser_whitelist_movie':0,
        'multiuser_whitelist_episode':0,
        'multiuser_whitelist_audio':0,
        'multiuser_whitelist_audiobook':0,

        'blacktag':'',

        'delete_blacktagged_movie':0,
        'delete_blacktagged_episode':0,
        'delete_blacktagged_audio':0,
        'delete_blacktagged_audiobook':0,

        'whitetag':'',

        'minimum_number_episodes':0,
        'minimum_number_played_episodes':0,
        'minimum_number_episodes_behavior':'Min Played Min Unplayed',

        'keep_favorites_advanced_movie_genre':0,
        'keep_favorites_advanced_movie_library_genre':0,

        'keep_favorites_advanced_episode_genre':0,
        'keep_favorites_advanced_season_genre':0,
        'keep_favorites_advanced_series_genre':0,
        'keep_favorites_advanced_tv_library_genre':0,
        'keep_favorites_advanced_tv_studio_network':0,
        'keep_favorites_advanced_tv_studio_network_genre':0,

        'keep_favorites_advanced_track_genre':0,
        'keep_favorites_advanced_album_genre':0,
        'keep_favorites_advanced_music_library_genre':0,
        'keep_favorites_advanced_track_artist':0,
        'keep_favorites_advanced_album_artist':0,

        'keep_favorites_advanced_audio_book_track_genre':0,
        'keep_favorites_advanced_audio_book_genre':0,
        'keep_favorites_advanced_audio_book_library_genre':0,
        'keep_favorites_advanced_audio_book_track_author':0,
        'keep_favorites_advanced_audio_book_author':0,
        'keep_favorites_advanced_audio_book_library_author':0,

        'print_script_header':True,
        'print_warnings':True,
        'print_user_header':True,
        'print_movie_delete_info':True,
        'print_movie_keep_info':True,
        'print_movie_error_info':True,
        'print_episode_delete_info':True,
        'print_episode_keep_info':True,
        'print_episode_error_info':True,
        'print_audio_delete_info':True,
        'print_audio_keep_info':True,
        'print_audio_error_info':True,
        'print_audiobook_delete_info':True,
        'print_audiobook_keep_info':True,
        'print_audiobook_error_info':True,
        'print_summary_header':True,
        'print_movie_summary':True,
        'print_episode_summary':True,
        'print_audio_summary':True,
        'print_audiobook_summary':True,

        'movie_set_missing_last_played_date':1,
        'episode_set_missing_last_played_date':1,
        'audio_set_missing_last_played_date':1,
        'audiobook_set_missing_last_played_date':1,

        #------------API Cache Maximum Size-------------#

        'api_query_cache_size':20
    }


#get default configuration values
def get_default_config_values(config_value):

    #preConfigDebug = True
    preConfigDebug = False
    
    #DEBUG
    if (preConfigDebug):
        print(str(config_value) + '=' + str(defaultConfigValues[config_value]))

    return(defaultConfigValues[config_value])
