#!/usr/bin/env python3
from mumc_modules.mumc_output import print_byType
from mumc_modules.mumc_setup_questions import get_brand,get_url,get_port,get_base,get_admin_username,get_admin_password,get_library_setup_behavior,get_library_matching_behavior,get_tag_name,get_authentication_key
from mumc_modules.mumc_versions import get_script_version
from mumc_modules.mumc_console_info import print_all_media_disabled,build_new_config_setup_to_delete_media
from mumc_modules.mumc_configuration_yaml import yaml_configurationBuilder
from mumc_modules.mumc_config_updater import yaml_configurationUpdater
from mumc_modules.mumc_config_skeleton import setYAMLConfigSkeleton
from mumc_modules.mumc_userlib_builder import get_users_and_libraries
from mumc_modules.mumc_init import getIsAnyMediaEnabled


#get user input needed to build or edit the mumc_config.yaml file
def build_configuration_file(the_dict):

    print('----------------------------------------------------------------------------------------')
    print('Version: ' + get_script_version())

    #Building the config
    if (not the_dict['advanced_settings']['UPDATE_CONFIG']):
        print('----------------------------------------------------------------------------------------')
        #ask user for server brand (i.e. emby or jellyfin)
        the_dict['admin_settings']={}
        the_dict['admin_settings']['server']={}
        the_dict['admin_settings']['server']['brand']=get_brand()
        the_dict['server_brand']=the_dict['admin_settings']['server']['brand']
        the_dict['UPDATE_CONFIG']=the_dict['advanced_settings']['UPDATE_CONFIG']
        the_dict=setYAMLConfigSkeleton(the_dict)
        the_dict['admin_settings']['server']['brand']=the_dict['server_brand']
        the_dict['advanced_settings']['UPDATE_CONFIG']=the_dict['UPDATE_CONFIG']
        the_dict.pop('server_brand')
        the_dict.pop('UPDATE_CONFIG')

        print('----------------------------------------------------------------------------------------')
        #ask user for server's url
        the_dict['server']=get_url()
        print('----------------------------------------------------------------------------------------')
        #ask user for the emby or jellyfin port number
        the_dict['port']=get_port()
        print('----------------------------------------------------------------------------------------')
        #ask user for url-base
        the_dict['server_base']=get_base(the_dict['admin_settings']['server']['brand'])
        if (len(the_dict['port'])):
            the_dict['admin_settings']['server']['url']=the_dict['server'] + ':' + the_dict['port'] + '/' + the_dict['server_base']
        else:
            the_dict['admin_settings']['server']['url']=the_dict['server'] + '/' + the_dict['server_base']
        #Remove server, port, and server_base so they cannot be used later
        the_dict.pop('server')
        the_dict.pop('port')
        the_dict.pop('server_base')
        print('----------------------------------------------------------------------------------------')

        #ask user for administrator username
        the_dict['username']=get_admin_username()
        print('----------------------------------------------------------------------------------------')
        #ask user for administrator password
        the_dict['password']=get_admin_password()
        print('----------------------------------------------------------------------------------------')
        #ask server for authentication key using administrator username and password
        the_dict['admin_settings']['server']['auth_key']=get_authentication_key(the_dict['username'],the_dict['password'],the_dict)
        #Remove username and password so they cannot be used later
        the_dict.pop('username')
        the_dict.pop('password')

        #ask user how they want to choose libraries/folders
        the_dict['admin_settings']['behavior']['list']=get_library_setup_behavior()
        print('----------------------------------------------------------------------------------------')

        #ask user how they want media items to be matched to libraries/folders
        the_dict['admin_settings']['behavior']['matching']=get_library_matching_behavior()
        print('----------------------------------------------------------------------------------------')

        #Initialize for compare with other tag to prevent using the same tag in both blacktag and whitetag
        the_dict['advanced_settings']['blacktags']=[]
        the_dict['advanced_settings']['whitetags']=[]

        #ask user for global blacktag(s)
        the_dict['advanced_settings']['blacktags']=get_tag_name('blacktag',the_dict['advanced_settings']['whitetags'])
        print('----------------------------------------------------------------------------------------')

        #ask user for global whitetag(s)
        the_dict['advanced_settings']['whitetags']=get_tag_name('whitetag',the_dict['advanced_settings']['blacktags'])
        print('----------------------------------------------------------------------------------------')

    #Updating the config; Prepare to run the config editor
    else: #(the_dict['advanced_settings']['UPDATE_CONFIG']):
        print('----------------------------------------------------------------------------------------')
        #ask user how they want to choose libraries/folders
        #library_setup_behavior=get_library_setup_behavior(cfg.library_setup_behavior)
        the_dict['admin_settings']['behavior']['list']=get_library_setup_behavior(the_dict['admin_settings']['behavior']['list'])
        print('----------------------------------------------------------------------------------------')
        #ask user how they want media items to be matched to libraries/folders
        #library_matching_behavior=get_library_matching_behavior(cfg.library_matching_behavior.casefold())
        the_dict['admin_settings']['behavior']['matching']=get_library_matching_behavior(the_dict['admin_settings']['behavior']['matching'])
        print('----------------------------------------------------------------------------------------')

    #run the user and library selector; ask user to select user and associate desired libraries to be monitored for each
    the_dict['admin_settings']['users']=get_users_and_libraries(the_dict)
    print('----------------------------------------------------------------------------------------')

    #set REMOVE_FILES
    the_dict['advanced_settings']['REMOVE_FILES']=False

    print('----------------------------------------------------------------------------------------')
    
    #Build and save yaml config file
    if (not the_dict['advanced_settings']['UPDATE_CONFIG']):
        yaml_configurationBuilder(the_dict)
    else: #(the_dict['advanced_settings']['UPDATE_CONFIG']):
        yaml_configurationUpdater(the_dict)

    #Check config editing was not requested
    if not (the_dict['advanced_settings']['UPDATE_CONFIG']):
        try:
            the_dict=getIsAnyMediaEnabled(the_dict)
            if (the_dict['all_media_disabled']):
                print_all_media_disabled(the_dict)

            try:
                strings_list_to_print=['']
                strings_list_to_print=build_new_config_setup_to_delete_media(strings_list_to_print,the_dict)
                print_byType(strings_list_to_print[0],the_dict['advanced_settings']['console_controls']['warnings']['script']['show'],the_dict,the_dict['advanced_settings']['console_controls']['warnings']['script']['formatting'])
            except:
                the_dict['advanced_settings']['console_controls']['warnings']['script']['show']=True
                the_dict['advanced_settings']['console_controls']['warnings']['script']['formatting']['font']['color']=''
                the_dict['advanced_settings']['console_controls']['warnings']['script']['formatting']['font']['style']=''
                the_dict['advanced_settings']['console_controls']['warnings']['script']['formatting']['background']['color']=''
                strings_list_to_print=['']
                strings_list_to_print=build_new_config_setup_to_delete_media(strings_list_to_print,the_dict)
                print_byType(strings_list_to_print[0],the_dict['advanced_settings']['console_controls']['warnings']['script']['show'],the_dict,the_dict['advanced_settings']['console_controls']['warnings']['script']['formatting'])

        #the exception
        except (AttributeError, ModuleNotFoundError):
            #something went wrong
            #mumc_config.yaml should have been created by now
            #we are here because the mumc_config.yaml file does not exist
            #this is either the first time the script is running or mumc_config.yaml file was deleted

            #raise error
            raise RuntimeError('\nConfigError: Cannot find or open mumc_config.yaml')


#get user input needed to edit the mumc_config.yaml file
def edit_configuration_file(cfg):
    build_configuration_file(cfg)