#!/usr/bin/env python3
from mumc_modules.mumc_output import appendTo_DEBUG_log
from mumc_modules.mumc_compare_items import get_isItemMatching_doesItemStartWith
from mumc_modules.mumc_played_created import get_playedCreatedDays_playedCreatedCounts
from mumc_modules.mumc_item_info import get_ADDITIONAL_itemInfo


#Determine if media item whitelisted for the current user or for another user
def get_isItemWhitelisted_Blacklisted(baselist,checklist,item,user_info,var_dict,the_dict):

    LibraryID=var_dict['this_' + baselist + '_lib']['lib_id']
    LibraryNetPath=var_dict['this_' + baselist + '_lib']['network_path']
    LibraryPath=var_dict['this_' + baselist + '_lib']['path']
    #library_matching_behavior=var_dict['library_matching_behavior']
    library_matching_behavior=the_dict['admin_settings']['behavior']['matching']

    #user_wllib_key_json=user_wllib_keys_json[var_dict['currentUserPosition']]
    #user_wllib_netpath_json=user_wllib_netpath_json[var_dict['currentUserPosition']]
    #user_wllib_path_json=user_wllib_path_json[var_dict['currentUserPosition']]
    user_wllib_key_json=[]
    user_wllib_netpath_json=[]
    user_wllib_path_json=[]
    for looplist in user_info[checklist]:
        if (library_matching_behavior == 'byid'):
            user_wllib_key_json.append(looplist['lib_id'])
        elif (library_matching_behavior == 'bynetworkpath'):
            user_wllib_netpath_json.append(looplist['network_path'])
        elif (library_matching_behavior == 'bypath'):
            user_wllib_path_json.append(looplist['path'])

    item_isWhitelisted=False
    itemWhitelistedValue=''

    #DEBUG log formatting
    if (the_dict['DEBUG']):
        appendTo_DEBUG_log("\n",1,the_dict)

    if (library_matching_behavior == 'byid'):
        #item_isWhitelisted, itemWhitelistedValue=get_isItemMatching_doesItemStartWith(LibraryID,user_wllib_key_json,the_dict)
        item_isWhitelisted, itemWhitelistedValue=get_isItemMatching_doesItemStartWith(LibraryID,','.join(map(str, user_wllib_key_json)),the_dict)
    elif (library_matching_behavior == 'bypath'):
        if ("Path" in item):
            ItemPath = item["Path"]
        elif (("MediaSources" in item) and ("Path" in item["MediaSources"])):
            ItemPath = item["MediaSources"]["Path"]
        else:
            ItemPath = LibraryPath
        item_isWhitelisted, itemWhitelistedValue=get_isItemMatching_doesItemStartWith(ItemPath,user_wllib_path_json,the_dict)
    elif (library_matching_behavior == 'bynetworkpath'):
        if ("Path" in item):
            ItemNetPath = item["Path"]
        elif (("MediaSources" in item) and ("Path" in item["MediaSources"])):
            ItemNetPath = item["MediaSources"]["Path"]
        else:
            ItemNetPath = LibraryNetPath
        item_isWhitelisted, itemWhitelistedValue=get_isItemMatching_doesItemStartWith(ItemNetPath,user_wllib_netpath_json,the_dict)

    if (the_dict['DEBUG']):
        appendTo_DEBUG_log('\nItem is whitelisted/blacklisted for this user: ' + str(item_isWhitelisted),2,the_dict)
        appendTo_DEBUG_log('\nMatching whitelisted/blacklisted value for this user is: ' + str(itemWhitelistedValue),2,the_dict)
        appendTo_DEBUG_log('\nLibraryId is: ' + LibraryID,2,the_dict)
        appendTo_DEBUG_log('\nLibraryPath is: ' + LibraryPath,2,the_dict)
        appendTo_DEBUG_log('\nLibraryNetPath is: ' + LibraryNetPath,2,the_dict)
        appendTo_DEBUG_log('\nWhitelisted/Blacklisted Keys are: ' + ','.join(map(str, user_wllib_key_json)),2,the_dict)
        appendTo_DEBUG_log('\nWhitelisted/Blacklisted Paths are: ' + ','.join(map(str, user_wllib_path_json)),2,the_dict)
        appendTo_DEBUG_log('\nWhitelisted/Blacklisted NetworkPaths are: ' + ','.join(map(str, user_wllib_netpath_json)),2,the_dict)

    return item_isWhitelisted


#def whitelist_playedPatternCleanup(the_dict,itemsDictionary,itemsExtraDictionary,postproc_dict):
#def whitelist_playedPatternCleanup(prefix_str,postproc_dict,the_dict):
    #whiteblack_dict={}

    #whiteblack_dict['library_matching_behavior']=postproc_dict['library_matching_behavior']
    #whiteblack_dict['wl_bl_user_keys_json_verify']=postproc_dict['wluser_keys_json_verify']
    #whiteblack_dict['user_wl_bl_lib_keys_json']=postproc_dict['user_wllib_keys_json']
    #whiteblack_dict['user_wl_bl_lib_netpath_json']=postproc_dict['user_wllib_netpath_json']
    #whiteblack_dict['user_wl_bl_lib_path_json']=postproc_dict['user_wllib_path_json']

    #return whitelist_and_blacklist_playedPatternCleanup(the_dict,itemsDictionary,itemsExtraDictionary,whiteblack_dict)
    #return whitelist_and_blacklist_playedPatternCleanup(prefix_str,postproc_dict,the_dict)


#Because we are not searching directly for unplayed black/whitelisted items; cleanup needs to happen to help the behavioral patterns make sense
def whitelist_and_blacklist_playedPatternCleanup(prefix_str,postproc_dict,the_dict):
    itemId_tracker=[]

    itemsDictionary=postproc_dict['is' + prefix_str + '_and_played_byUserId_Media']
    itemsExtraDictionary=postproc_dict['is' + prefix_str + '_extraInfo_byUserId_Media']
    #library_matching_behavior=postproc_dict['library_matching_behavior']
    postproc_dict['user_info']=the_dict['admin_settings']['users']
    #user_wl_bl_lib_keys_json=postproc_dict['user_bllib_keys_json']
    #user_wl_bl_lib_netpath_json=postproc_dict['user_bllib_netpath_json']
    #user_wl_bl_lib_path_json=postproc_dict['user_bllib_path_json']
    baselist=prefix_str[0:prefix_str.rfind("ed")]
    checklist=baselist

    played_created_days_counts_dict={}

    if (('MonitoredUsersAction' in itemsExtraDictionary) and ('MonitoredUsersMeetPlayedFilter' in itemsExtraDictionary)):

        for userId in itemsDictionary:
            for itemId in itemsDictionary[userId]:
                if not (itemId in itemId_tracker):
                    itemId_tracker.append(itemId)
                    item=itemsDictionary[userId][itemId]
                    for sub_user_info in postproc_dict['user_info']:
                        if (not(userId == sub_user_info['user_id'])):
                            if (not(item['Id'] in itemsDictionary[sub_user_info['user_id']])):
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]={}
                                if (the_dict['DEBUG']):
                                    appendTo_DEBUG_log("\nAdd missing itemid " + str(item['Id']) + " to " + str(itemsExtraDictionary[sub_user_info['user_id']]),3,the_dict)
                            if (not('IsMeetingAction' in itemsExtraDictionary[sub_user_info['user_id']][item['Id']])):

                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingAction']=get_isItemWhitelisted_Blacklisted(baselist,checklist,item,sub_user_info,var_dict,the_dict)
                                '''
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingAction']=get_isItemWhitelisted_Blacklisted(the_dict,item,
                                itemsExtraDictionary[userId][item['Id']]['WhitelistBlacklistLibraryId'],
                                itemsExtraDictionary[userId][item['Id']]['WhitelistBlacklistLibraryNetPath'],
                                itemsExtraDictionary[userId][item['Id']]['WhitelistBlacklistLibraryPath'],
                                prefix_str,library_matching_behavior,postproc_dict['user_info'].index(sub_user_info['user_id']),
                                postproc_dict['user_info'].index(sub_user_info['user_id']),
                                postproc_dict['user_info'].index(sub_user_info['user_id']))
                                '''
                                if (the_dict['DEBUG']):
                                    appendTo_DEBUG_log("\nIsMeetingAction: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingAction']),3,the_dict)
                            if (not('IsMeetingPlayedFilter' in itemsExtraDictionary[sub_user_info['user_id']][item['Id']])):
                                #if ((behaviorFilter == 0) or (behaviorFilter == 1) or (behaviorFilter == 2)):
                                    #itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingPlayedFilter']=True
                                #else:
                                mediaItemAdditionalInfo=get_ADDITIONAL_itemInfo(sub_user_info['user_id'],item['Id'],'playedPatternCleanup',the_dict)
                                played_created_days_counts_dict=get_playedCreatedDays_playedCreatedCounts(the_dict,mediaItemAdditionalInfo,itemsExtraDictionary[userId][item['Id']]['PlayedDays'],
                                itemsExtraDictionary[userId][item['Id']]['CreatedDays'],itemsExtraDictionary[userId][item['Id']]['CutOffDatePlayed'],itemsExtraDictionary[userId][item['Id']]['CutOffDateCreated'],
                                itemsExtraDictionary[userId][item['Id']]['PlayedCountComparison'],itemsExtraDictionary[userId][item['Id']]['PlayedCount'],itemsExtraDictionary[userId][item['Id']]['CreatedPlayedCountComparison'],
                                itemsExtraDictionary[userId][item['Id']]['CreatedPlayedCount'])

                                #if (not (item_matches_played_days_filter == None)):
                                    #itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingPlayedFilter']=(item_matches_played_days_filter and item_matches_played_count_filter)
                                #else:
                                    #itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingPlayedFilter']=None
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['itemIsPlayed']=played_created_days_counts_dict['itemIsPlayed']
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['itemPlayedCount']=played_created_days_counts_dict['itemPlayedCount']
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_played_days_filter']=played_created_days_counts_dict['item_matches_played_days_filter'] #meeting played X days ago?
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_created_days_filter']=played_created_days_counts_dict['item_matches_created_days_filter'] #meeting created X days ago?
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_played_count_filter']=played_created_days_counts_dict['item_matches_played_count_filter'] #played X number of times?
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_created_played_count_filter']=played_created_days_counts_dict['item_matches_created_played_count_filter'] #created-played X number of times?
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingPlayedFilter']=(played_created_days_counts_dict['item_matches_played_days_filter'] and played_created_days_counts_dict['item_matches_played_count_filter']) #meeting complete played_filter_*?
                                itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingCreatedPlayedFilter']=(played_created_days_counts_dict['item_matches_created_days_filter'] and played_created_days_counts_dict['item_matches_created_played_count_filter']) #meeting complete created_filter_*?

                                if (the_dict['DEBUG']):
                                    appendTo_DEBUG_log("\itemIsPlayed: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['itemIsPlayed']),3,the_dict)
                                    appendTo_DEBUG_log("\itemPlayedCount: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['itemPlayedCount']),3,the_dict)
                                    appendTo_DEBUG_log("\item_matches_played_days_filter: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_played_days_filter']),3,the_dict)
                                    appendTo_DEBUG_log("\item_matches_created_days_filter: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_created_days_filter']),3,the_dict)
                                    appendTo_DEBUG_log("\item_matches_played_count_filter: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_played_count_filter']),3,the_dict)
                                    appendTo_DEBUG_log("\item_matches_created_played_count_filter: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['item_matches_created_played_count_filter']),3,the_dict)
                                    appendTo_DEBUG_log("\IsMeetingPlayedFilter: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingPlayedFilter']),3,the_dict)
                                    appendTo_DEBUG_log("\IsMeetingCreatedPlayedFilter: " + str(itemsExtraDictionary[sub_user_info['user_id']][item['Id']]['IsMeetingCreatedPlayedFilter']),3,the_dict)
                            if (not(item['Id'] in itemsDictionary[sub_user_info['user_id']])):
                                itemsDictionary[sub_user_info['user_id']][item['Id']]=get_ADDITIONAL_itemInfo(sub_user_info,item['Id'],'whitelist_playedPatternCleanup',the_dict)
                                if (the_dict['DEBUG']):
                                    appendTo_DEBUG_log("\Add item with id: " + str(item['Id']) + "to dictionary",3,the_dict)

    postproc_dict['is' + prefix_str + '_and_played_byUserId_Media']=itemsDictionary
    postproc_dict['is' + prefix_str + '_extraInfo_byUserId_Media']=itemsExtraDictionary

    return postproc_dict