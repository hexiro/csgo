# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base_gcmessages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import csgo.protobufs.steammessages_pb2 as steammessages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62\x61se_gcmessages.proto\x12\x04\x63sgo\x1a\x13steammessages.proto\"}\n\x1d\x43GCStorePurchaseInit_LineItem\x12\x13\n\x0bitem_def_id\x18\x01 \x01(\r\x12\x10\n\x08quantity\x18\x02 \x01(\r\x12\x1e\n\x16\x63ost_in_local_currency\x18\x03 \x01(\r\x12\x15\n\rpurchase_type\x18\x04 \x01(\r\"\x87\x01\n\x17\x43MsgGCStorePurchaseInit\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\x05\x12\x10\n\x08\x63urrency\x18\x03 \x01(\x05\x12\x37\n\nline_items\x18\x04 \x03(\x0b\x32#.csgo.CGCStorePurchaseInit_LineItem\"`\n\x1f\x43MsgGCStorePurchaseInitResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0e\n\x06txn_id\x18\x02 \x01(\x04\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x10\n\x08item_ids\x18\x04 \x03(\x04\"P\n\x0e\x43SOPartyInvite\x12\x16\n\x08group_id\x18\x01 \x01(\x04\x42\x04\x80\xa6\x1d\x01\x12\x11\n\tsender_id\x18\x02 \x01(\x06\x12\x13\n\x0bsender_name\x18\x03 \x01(\t\"P\n\x0e\x43SOLobbyInvite\x12\x16\n\x08group_id\x18\x01 \x01(\x04\x42\x04\x80\xa6\x1d\x01\x12\x11\n\tsender_id\x18\x02 \x01(\x06\x12\x13\n\x0bsender_name\x18\x03 \x01(\t\"&\n\x13\x43MsgSystemBroadcast\x12\x0f\n\x07message\x18\x01 \x01(\t\"R\n\x11\x43MsgInviteToParty\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x16\n\x0e\x63lient_version\x18\x02 \x01(\r\x12\x13\n\x0bteam_invite\x18\x03 \x01(\r\";\n\x15\x43MsgInvitationCreated\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12\x10\n\x08steam_id\x18\x02 \x01(\x06\"h\n\x17\x43MsgPartyInviteResponse\x12\x10\n\x08party_id\x18\x01 \x01(\x04\x12\x0e\n\x06\x61\x63\x63\x65pt\x18\x02 \x01(\x08\x12\x16\n\x0e\x63lient_version\x18\x03 \x01(\r\x12\x13\n\x0bteam_invite\x18\x04 \x01(\r\"%\n\x11\x43MsgKickFromParty\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\"\x10\n\x0e\x43MsgLeaveParty\"\x15\n\x13\x43MsgServerAvailable\"*\n\x16\x43MsgLANServerAvailable\x12\x10\n\x08lobby_id\x18\x01 \x01(\x06\"\xb4\x01\n\x18\x43SOEconGameAccountClient\x12$\n\x19\x61\x64\x64itional_backpack_slots\x18\x01 \x01(\r:\x01\x30\x12\"\n\x1a\x62onus_xp_timestamp_refresh\x18\x0c \x01(\x07\x12\x1a\n\x12\x62onus_xp_usedflags\x18\r \x01(\r\x12\x16\n\x0e\x65levated_state\x18\x0e \x01(\r\x12\x1a\n\x12\x65levated_timestamp\x18\x0f \x01(\r\"r\n\x18\x43SOItemCriteriaCondition\x12\n\n\x02op\x18\x01 \x01(\x05\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x10\n\x08required\x18\x03 \x01(\x08\x12\x13\n\x0b\x66loat_value\x18\x04 \x01(\x02\x12\x14\n\x0cstring_value\x18\x05 \x01(\t\"\xb6\x02\n\x0f\x43SOItemCriteria\x12\x12\n\nitem_level\x18\x01 \x01(\r\x12\x14\n\x0citem_quality\x18\x02 \x01(\x05\x12\x16\n\x0eitem_level_set\x18\x03 \x01(\x08\x12\x18\n\x10item_quality_set\x18\x04 \x01(\x08\x12\x19\n\x11initial_inventory\x18\x05 \x01(\r\x12\x18\n\x10initial_quantity\x18\x06 \x01(\r\x12\x1b\n\x13ignore_enabled_flag\x18\x08 \x01(\x08\x12\x32\n\nconditions\x18\t \x03(\x0b\x32\x1e.csgo.CSOItemCriteriaCondition\x12\x13\n\x0bitem_rarity\x18\n \x01(\x05\x12\x17\n\x0fitem_rarity_set\x18\x0b \x01(\x08\x12\x13\n\x0brecent_only\x18\x0c \x01(\x08\"\xdf\x03\n\rCSOItemRecipe\x12\x11\n\tdef_index\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03n_a\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65sc_inputs\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x65sc_outputs\x18\x05 \x01(\t\x12\x0c\n\x04\x64i_a\x18\x06 \x01(\t\x12\x0c\n\x04\x64i_b\x18\x07 \x01(\t\x12\x0c\n\x04\x64i_c\x18\x08 \x01(\t\x12\x0c\n\x04\x64o_a\x18\t \x01(\t\x12\x0c\n\x04\x64o_b\x18\n \x01(\t\x12\x0c\n\x04\x64o_c\x18\x0b \x01(\t\x12\x1f\n\x17requires_all_same_class\x18\x0c \x01(\x08\x12\x1e\n\x16requires_all_same_slot\x18\r \x01(\x08\x12\x1e\n\x16\x63lass_usage_for_output\x18\x0e \x01(\x05\x12\x1d\n\x15slot_usage_for_output\x18\x0f \x01(\x05\x12\x16\n\x0eset_for_output\x18\x10 \x01(\x05\x12\x33\n\x14input_items_criteria\x18\x14 \x03(\x0b\x32\x15.csgo.CSOItemCriteria\x12\x34\n\x15output_items_criteria\x18\x15 \x03(\x0b\x32\x15.csgo.CSOItemCriteria\x12\x1e\n\x16input_item_dupe_counts\x18\x16 \x03(\r\"R\n\x15\x43MsgDevNewItemRequest\x12\x10\n\x08receiver\x18\x01 \x01(\x06\x12\'\n\x08\x63riteria\x18\x02 \x01(\x0b\x32\x15.csgo.CSOItemCriteria\"\x8c\x01\n\x1f\x43MsgIncrementKillCountAttribute\x12\x19\n\x11killer_account_id\x18\x01 \x01(\x07\x12\x19\n\x11victim_account_id\x18\x02 \x01(\x07\x12\x0f\n\x07item_id\x18\x03 \x01(\x04\x12\x12\n\nevent_type\x18\x04 \x01(\r\x12\x0e\n\x06\x61mount\x18\x05 \x01(\r\"\x86\x01\n\x10\x43MsgApplySticker\x12\x17\n\x0fsticker_item_id\x18\x01 \x01(\x04\x12\x14\n\x0citem_item_id\x18\x02 \x01(\x04\x12\x14\n\x0csticker_slot\x18\x03 \x01(\r\x12\x17\n\x0f\x62\x61seitem_defidx\x18\x04 \x01(\r\x12\x14\n\x0csticker_wear\x18\x05 \x01(\x02\"S\n\x17\x43MsgModifyItemAttribute\x12\x0f\n\x07item_id\x18\x01 \x01(\x04\x12\x13\n\x0b\x61ttr_defidx\x18\x02 \x01(\r\x12\x12\n\nattr_value\x18\x03 \x01(\r\"]\n\x15\x43MsgApplyStatTrakSwap\x12\x14\n\x0ctool_item_id\x18\x01 \x01(\x04\x12\x16\n\x0eitem_1_item_id\x18\x02 \x01(\x04\x12\x16\n\x0eitem_2_item_id\x18\x03 \x01(\x04\"J\n\x14\x43MsgApplyStrangePart\x12\x1c\n\x14strange_part_item_id\x18\x01 \x01(\x04\x12\x14\n\x0citem_item_id\x18\x02 \x01(\x04\"K\n\x17\x43MsgApplyPennantUpgrade\x12\x17\n\x0fupgrade_item_id\x18\x01 \x01(\x04\x12\x17\n\x0fpennant_item_id\x18\x02 \x01(\x04\"C\n\x13\x43MsgApplyEggEssence\x12\x17\n\x0f\x65ssence_item_id\x18\x01 \x01(\x04\x12\x13\n\x0b\x65gg_item_id\x18\x02 \x01(\x04\"M\n\x14\x43SOEconItemAttribute\x12\x11\n\tdef_index\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\x12\x13\n\x0bvalue_bytes\x18\x03 \x01(\x0c\":\n\x13\x43SOEconItemEquipped\x12\x11\n\tnew_class\x18\x01 \x01(\r\x12\x10\n\x08new_slot\x18\x02 \x01(\r\"\xae\x03\n\x0b\x43SOEconItem\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x12\n\naccount_id\x18\x02 \x01(\r\x12\x11\n\tinventory\x18\x03 \x01(\r\x12\x11\n\tdef_index\x18\x04 \x01(\r\x12\x10\n\x08quantity\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r\x12\x0f\n\x07quality\x18\x07 \x01(\r\x12\x10\n\x05\x66lags\x18\x08 \x01(\r:\x01\x30\x12\x0e\n\x06origin\x18\t \x01(\r\x12\x13\n\x0b\x63ustom_name\x18\n \x01(\t\x12\x13\n\x0b\x63ustom_desc\x18\x0b \x01(\t\x12-\n\tattribute\x18\x0c \x03(\x0b\x32\x1a.csgo.CSOEconItemAttribute\x12(\n\rinterior_item\x18\r \x01(\x0b\x32\x11.csgo.CSOEconItem\x12\x15\n\x06in_use\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05style\x18\x0f \x01(\r:\x01\x30\x12\x16\n\x0boriginal_id\x18\x10 \x01(\x04:\x01\x30\x12\x31\n\x0e\x65quipped_state\x18\x12 \x03(\x0b\x32\x19.csgo.CSOEconItemEquipped\x12\x0e\n\x06rarity\x18\x13 \x01(\r\"a\n\x1b\x43MsgAdjustItemEquippedState\x12\x0f\n\x07item_id\x18\x01 \x01(\x04\x12\x11\n\tnew_class\x18\x02 \x01(\r\x12\x10\n\x08new_slot\x18\x03 \x01(\r\x12\x0c\n\x04swap\x18\x04 \x01(\x08\"^\n CMsgAdjustItemEquippedStateMulti\x12\x10\n\x08t_equips\x18\x01 \x03(\x04\x12\x11\n\tct_equips\x18\x02 \x03(\x04\x12\x15\n\rnoteam_equips\x18\x03 \x03(\x04\"\"\n\rCMsgSortItems\x12\x11\n\tsort_type\x18\x01 \x01(\r\"^\n\x10\x43SOEconClaimCode\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x11\n\tcode_type\x18\x02 \x01(\r\x12\x15\n\rtime_acquired\x18\x03 \x01(\r\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\"E\n\x14\x43MsgStoreGetUserData\x12\x1b\n\x13price_sheet_version\x18\x01 \x01(\x07\x12\x10\n\x08\x63urrency\x18\x02 \x01(\x05\"\x99\x01\n\x1c\x43MsgStoreGetUserDataResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x1b\n\x13\x63urrency_deprecated\x18\x02 \x01(\x05\x12\x1a\n\x12\x63ountry_deprecated\x18\x03 \x01(\t\x12\x1b\n\x13price_sheet_version\x18\x04 \x01(\x07\x12\x13\n\x0bprice_sheet\x18\x08 \x01(\x0c\"\x86\x01\n\x14\x43MsgUpdateItemSchema\x12\x12\n\nitems_game\x18\x01 \x01(\x0c\x12\x1b\n\x13item_schema_version\x18\x02 \x01(\x07\x12%\n\x1ditems_game_url_DEPRECATED2013\x18\x03 \x01(\t\x12\x16\n\x0eitems_game_url\x18\x04 \x01(\t\"!\n\x0b\x43MsgGCError\x12\x12\n\nerror_text\x18\x01 \x01(\t\"\x1d\n\x1b\x43MsgRequestInventoryRefresh\".\n\x0f\x43MsgConVarValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\">\n\x14\x43MsgReplicateConVars\x12&\n\x07\x63onvars\x18\x01 \x03(\x0b\x32\x15.csgo.CMsgConVarValue\"\x8e\x01\n\x0b\x43MsgUseItem\x12\x0f\n\x07item_id\x18\x01 \x01(\x04\x12\x17\n\x0ftarget_steam_id\x18\x02 \x01(\x06\x12\x1f\n\x17gift__potential_targets\x18\x03 \x03(\r\x12\x18\n\x10\x64uel__class_lock\x18\x04 \x01(\r\x12\x1a\n\x12initiator_steam_id\x18\x05 \x01(\x06\"d\n\x1b\x43MsgReplayUploadedToYouTube\x12\x13\n\x0byoutube_url\x18\x01 \x01(\t\x12\x1c\n\x14youtube_account_name\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\x04\".\n\x17\x43MsgConsumableExhausted\x12\x13\n\x0bitem_def_id\x18\x01 \x01(\x05\"\x9e\x01\n CMsgItemAcknowledged__DEPRECATED\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x11\n\tinventory\x18\x02 \x01(\r\x12\x11\n\tdef_index\x18\x03 \x01(\r\x12\x0f\n\x07quality\x18\x04 \x01(\r\x12\x0e\n\x06rarity\x18\x05 \x01(\r\x12\x0e\n\x06origin\x18\x06 \x01(\r\x12\x0f\n\x07item_id\x18\x07 \x01(\x04\"\xa2\x01\n\x14\x43MsgSetItemPositions\x12?\n\x0eitem_positions\x18\x01 \x03(\x0b\x32\'.csgo.CMsgSetItemPositions.ItemPosition\x1aI\n\x0cItemPosition\x12\x16\n\x0elegacy_item_id\x18\x01 \x01(\r\x12\x10\n\x08position\x18\x02 \x01(\r\x12\x0f\n\x07item_id\x18\x03 \x01(\x04\"\xb8\x01\n\x11\x43MsgGCReportAbuse\x12\x17\n\x0ftarget_steam_id\x18\x01 \x01(\x06\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0b\n\x03gid\x18\x05 \x01(\x04\x12\x12\n\nabuse_type\x18\x02 \x01(\r\x12\x14\n\x0c\x63ontent_type\x18\x03 \x01(\r\x12\x1d\n\x15target_game_server_ip\x18\x06 \x01(\x07\x12\x1f\n\x17target_game_server_port\x18\x07 \x01(\r\"[\n\x19\x43MsgGCReportAbuseResponse\x12\x17\n\x0ftarget_steam_id\x18\x01 \x01(\x06\x12\x0e\n\x06result\x18\x02 \x01(\r\x12\x15\n\rerror_message\x18\x03 \x01(\t\"f\n\x1a\x43MsgGCNameItemNotification\x12\x16\n\x0eplayer_steamid\x18\x01 \x01(\x06\x12\x16\n\x0eitem_def_index\x18\x02 \x01(\r\x12\x18\n\x10item_name_custom\x18\x03 \x01(\t\"\xb6\x01\n\x1f\x43MsgGCClientDisplayNotification\x12+\n#notification_title_localization_key\x18\x01 \x01(\t\x12*\n\"notification_body_localization_key\x18\x02 \x01(\t\x12\x1b\n\x13\x62ody_substring_keys\x18\x03 \x03(\t\x12\x1d\n\x15\x62ody_substring_values\x18\x04 \x03(\t\"1\n\x17\x43MsgGCShowItemsPickedUp\x12\x16\n\x0eplayer_steamid\x18\x01 \x01(\x06\"|\n CMsgGCIncrementKillCountResponse\x12\x1f\n\x11killer_account_id\x18\x01 \x01(\rB\x04\x80\xa6\x1d\x01\x12\x11\n\tnum_kills\x18\x02 \x01(\r\x12\x10\n\x08item_def\x18\x03 \x01(\r\x12\x12\n\nlevel_type\x18\x04 \x01(\r\"\x8f\x01\n\x18\x43SOEconItemDropRateBonus\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x17\n\x0f\x65xpiration_date\x18\x02 \x01(\x07\x12\r\n\x05\x62onus\x18\x03 \x01(\x02\x12\x13\n\x0b\x62onus_count\x18\x04 \x01(\r\x12\x0f\n\x07item_id\x18\x05 \x01(\x04\x12\x11\n\tdef_index\x18\x06 \x01(\r\"p\n\x19\x43SOEconItemLeagueViewPass\x12\x18\n\naccount_id\x18\x01 \x01(\rB\x04\x80\xa6\x1d\x01\x12\x17\n\tleague_id\x18\x02 \x01(\rB\x04\x80\xa6\x1d\x01\x12\r\n\x05\x61\x64min\x18\x03 \x01(\r\x12\x11\n\titemindex\x18\x04 \x01(\r\"O\n\x16\x43SOEconItemEventTicket\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\r\x12\x0f\n\x07item_id\x18\x03 \x01(\x04\"A\n\'CMsgGCItemPreviewItemBoughtNotification\x12\x16\n\x0eitem_def_index\x18\x01 \x01(\r\"+\n\x19\x43MsgGCStorePurchaseCancel\x12\x0e\n\x06txn_id\x18\x01 \x01(\x04\"3\n!CMsgGCStorePurchaseCancelResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\"-\n\x1b\x43MsgGCStorePurchaseFinalize\x12\x0e\n\x06txn_id\x18\x01 \x01(\x04\"G\n#CMsgGCStorePurchaseFinalizeResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x10\n\x08item_ids\x18\x02 \x03(\x04\"I\n\x1b\x43MsgGCBannedWordListRequest\x12\x19\n\x11\x62\x61n_list_group_id\x18\x01 \x01(\r\x12\x0f\n\x07word_id\x18\x02 \x01(\r\"\x1c\n\x1a\x43MsgGCRequestAnnouncements\"\x82\x01\n\"CMsgGCRequestAnnouncementsResponse\x12\x1a\n\x12\x61nnouncement_title\x18\x01 \x01(\t\x12\x14\n\x0c\x61nnouncement\x18\x02 \x01(\t\x12\x17\n\x0fnextmatch_title\x18\x03 \x01(\t\x12\x11\n\tnextmatch\x18\x04 \x01(\t\"z\n\x10\x43MsgGCBannedWord\x12\x0f\n\x07word_id\x18\x01 \x01(\r\x12G\n\tword_type\x18\x02 \x01(\x0e\x32\x17.csgo.GC_BannedWordType:\x1bGC_BANNED_WORD_DISABLE_WORD\x12\x0c\n\x04word\x18\x03 \x01(\t\"d\n\x1c\x43MsgGCBannedWordListResponse\x12\x19\n\x11\x62\x61n_list_group_id\x18\x01 \x01(\r\x12)\n\tword_list\x18\x02 \x03(\x0b\x32\x16.csgo.CMsgGCBannedWord\"Z\n!CMsgGCToGCBannedWordListBroadcast\x12\x35\n\tbroadcast\x18\x01 \x01(\x0b\x32\".csgo.CMsgGCBannedWordListResponse\"3\n\x1f\x43MsgGCToGCBannedWordListUpdated\x12\x10\n\x08group_id\x18\x01 \x01(\r\"\x92\x01\n.CSOEconDefaultEquippedDefinitionInstanceClient\x12\x18\n\naccount_id\x18\x01 \x01(\rB\x04\x80\xa6\x1d\x01\x12\x17\n\x0fitem_definition\x18\x02 \x01(\r\x12\x16\n\x08\x63lass_id\x18\x03 \x01(\rB\x04\x80\xa6\x1d\x01\x12\x15\n\x07slot_id\x18\x04 \x01(\rB\x04\x80\xa6\x1d\x01\"?\n\x17\x43MsgGCToGCDirtySDOCache\x12\x10\n\x08sdo_type\x18\x01 \x01(\r\x12\x12\n\nkey_uint64\x18\x02 \x01(\x04\"G\n\x1f\x43MsgGCToGCDirtyMultipleSDOCache\x12\x10\n\x08sdo_type\x18\x01 \x01(\r\x12\x12\n\nkey_uint64\x18\x02 \x03(\x04\"H\n\x11\x43MsgGCCollectItem\x12\x1a\n\x12\x63ollection_item_id\x18\x01 \x01(\x04\x12\x17\n\x0fsubject_item_id\x18\x02 \x01(\x04\"\x14\n\x12\x43MsgSDONoMemcached\"/\n\x1b\x43MsgGCToGCUpdateSQLKeyValue\x12\x10\n\x08key_name\x18\x01 \x01(\t\"-\n\x19\x43MsgGCToGCIsTrustedServer\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\"7\n!CMsgGCToGCIsTrustedServerResponse\x12\x12\n\nis_trusted\x18\x01 \x01(\x08\"8\n!CMsgGCToGCBroadcastConsoleCommand\x12\x13\n\x0b\x63on_command\x18\x01 \x01(\t\"4\n\x1a\x43MsgGCServerVersionUpdated\x12\x16\n\x0eserver_version\x18\x01 \x01(\r\"4\n\x1a\x43MsgGCClientVersionUpdated\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\r\" \n\x1e\x43MsgGCToGCWebAPIAccountChanged\"^\n\"CMsgGCToGCRequestPassportItemGrant\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x11\n\tleague_id\x18\x02 \x01(\r\x12\x13\n\x0breward_flag\x18\x03 \x01(\x05\"\xed\x04\n\x12\x43MsgGameServerInfo\x12\x1d\n\x15server_public_ip_addr\x18\x01 \x01(\x07\x12\x1e\n\x16server_private_ip_addr\x18\x02 \x01(\x07\x12\x13\n\x0bserver_port\x18\x03 \x01(\r\x12\x16\n\x0eserver_tv_port\x18\x04 \x01(\r\x12\x12\n\nserver_key\x18\x05 \x01(\t\x12\x1a\n\x12server_hibernation\x18\x06 \x01(\x08\x12\x45\n\x0bserver_type\x18\x07 \x01(\x0e\x32#.csgo.CMsgGameServerInfo.ServerType:\x0bUNSPECIFIED\x12\x15\n\rserver_region\x18\x08 \x01(\r\x12\x16\n\x0eserver_loadavg\x18\t \x01(\x02\x12 \n\x18server_tv_broadcast_time\x18\n \x01(\x02\x12\x18\n\x10server_game_time\x18\x0b \x01(\x02\x12\'\n\x1fserver_relay_connected_steam_id\x18\x0c \x01(\x06\x12\x17\n\x0frelay_slots_max\x18\r \x01(\r\x12\x18\n\x10relays_connected\x18\x0e \x01(\x05\x12\x1f\n\x17relay_clients_connected\x18\x0f \x01(\x05\x12$\n\x1crelayed_game_server_steam_id\x18\x10 \x01(\x06\x12\x1a\n\x12parent_relay_count\x18\x11 \x01(\r\x12\x16\n\x0etv_secret_code\x18\x12 \x01(\x06\"2\n\nServerType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04GAME\x10\x01\x12\t\n\x05PROXY\x10\x02*\xc7\x03\n\nEGCBaseMsg\x12\x1a\n\x15k_EMsgGCSystemMessage\x10\xa1\x1f\x12\x1d\n\x18k_EMsgGCReplicateConVars\x10\xa2\x1f\x12\x1a\n\x15k_EMsgGCConVarUpdated\x10\xa3\x1f\x12\x14\n\x0fk_EMsgGCInQueue\x10\xa8\x1f\x12\x1a\n\x15k_EMsgGCInviteToParty\x10\x95#\x12\x1e\n\x19k_EMsgGCInvitationCreated\x10\x96#\x12 \n\x1bk_EMsgGCPartyInviteResponse\x10\x97#\x12\x1a\n\x15k_EMsgGCKickFromParty\x10\x98#\x12\x17\n\x12k_EMsgGCLeaveParty\x10\x99#\x12\x1c\n\x17k_EMsgGCServerAvailable\x10\x9a#\x12\"\n\x1dk_EMsgGCClientConnectToServer\x10\x9b#\x12\x1b\n\x16k_EMsgGCGameServerInfo\x10\x9c#\x12\x12\n\rk_EMsgGCError\x10\x9d#\x12%\n k_EMsgGCReplay_UploadedToYouTube\x10\x9e#\x12\x1f\n\x1ak_EMsgGCLANServerAvailable\x10\x9f#*Y\n\x17\x45GCBaseProtoObjectTypes\x12\x1e\n\x19k_EProtoObjectPartyInvite\x10\xe9\x07\x12\x1e\n\x19k_EProtoObjectLobbyInvite\x10\xea\x07*T\n\x11GC_BannedWordType\x12\x1f\n\x1bGC_BANNED_WORD_DISABLE_WORD\x10\x00\x12\x1e\n\x1aGC_BANNED_WORD_ENABLE_WORD\x10\x01\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_gcmessages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001\220\001\000'
  _CSOPARTYINVITE.fields_by_name['group_id']._options = None
  _CSOPARTYINVITE.fields_by_name['group_id']._serialized_options = b'\200\246\035\001'
  _CSOLOBBYINVITE.fields_by_name['group_id']._options = None
  _CSOLOBBYINVITE.fields_by_name['group_id']._serialized_options = b'\200\246\035\001'
  _CMSGGCINCREMENTKILLCOUNTRESPONSE.fields_by_name['killer_account_id']._options = None
  _CMSGGCINCREMENTKILLCOUNTRESPONSE.fields_by_name['killer_account_id']._serialized_options = b'\200\246\035\001'
  _CSOECONITEMLEAGUEVIEWPASS.fields_by_name['account_id']._options = None
  _CSOECONITEMLEAGUEVIEWPASS.fields_by_name['account_id']._serialized_options = b'\200\246\035\001'
  _CSOECONITEMLEAGUEVIEWPASS.fields_by_name['league_id']._options = None
  _CSOECONITEMLEAGUEVIEWPASS.fields_by_name['league_id']._serialized_options = b'\200\246\035\001'
  _CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT.fields_by_name['account_id']._options = None
  _CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT.fields_by_name['account_id']._serialized_options = b'\200\246\035\001'
  _CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT.fields_by_name['class_id']._options = None
  _CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT.fields_by_name['class_id']._serialized_options = b'\200\246\035\001'
  _CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT.fields_by_name['slot_id']._options = None
  _CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT.fields_by_name['slot_id']._serialized_options = b'\200\246\035\001'
  _globals['_EGCBASEMSG']._serialized_start=8354
  _globals['_EGCBASEMSG']._serialized_end=8809
  _globals['_EGCBASEPROTOOBJECTTYPES']._serialized_start=8811
  _globals['_EGCBASEPROTOOBJECTTYPES']._serialized_end=8900
  _globals['_GC_BANNEDWORDTYPE']._serialized_start=8902
  _globals['_GC_BANNEDWORDTYPE']._serialized_end=8986
  _globals['_CGCSTOREPURCHASEINIT_LINEITEM']._serialized_start=52
  _globals['_CGCSTOREPURCHASEINIT_LINEITEM']._serialized_end=177
  _globals['_CMSGGCSTOREPURCHASEINIT']._serialized_start=180
  _globals['_CMSGGCSTOREPURCHASEINIT']._serialized_end=315
  _globals['_CMSGGCSTOREPURCHASEINITRESPONSE']._serialized_start=317
  _globals['_CMSGGCSTOREPURCHASEINITRESPONSE']._serialized_end=413
  _globals['_CSOPARTYINVITE']._serialized_start=415
  _globals['_CSOPARTYINVITE']._serialized_end=495
  _globals['_CSOLOBBYINVITE']._serialized_start=497
  _globals['_CSOLOBBYINVITE']._serialized_end=577
  _globals['_CMSGSYSTEMBROADCAST']._serialized_start=579
  _globals['_CMSGSYSTEMBROADCAST']._serialized_end=617
  _globals['_CMSGINVITETOPARTY']._serialized_start=619
  _globals['_CMSGINVITETOPARTY']._serialized_end=701
  _globals['_CMSGINVITATIONCREATED']._serialized_start=703
  _globals['_CMSGINVITATIONCREATED']._serialized_end=762
  _globals['_CMSGPARTYINVITERESPONSE']._serialized_start=764
  _globals['_CMSGPARTYINVITERESPONSE']._serialized_end=868
  _globals['_CMSGKICKFROMPARTY']._serialized_start=870
  _globals['_CMSGKICKFROMPARTY']._serialized_end=907
  _globals['_CMSGLEAVEPARTY']._serialized_start=909
  _globals['_CMSGLEAVEPARTY']._serialized_end=925
  _globals['_CMSGSERVERAVAILABLE']._serialized_start=927
  _globals['_CMSGSERVERAVAILABLE']._serialized_end=948
  _globals['_CMSGLANSERVERAVAILABLE']._serialized_start=950
  _globals['_CMSGLANSERVERAVAILABLE']._serialized_end=992
  _globals['_CSOECONGAMEACCOUNTCLIENT']._serialized_start=995
  _globals['_CSOECONGAMEACCOUNTCLIENT']._serialized_end=1175
  _globals['_CSOITEMCRITERIACONDITION']._serialized_start=1177
  _globals['_CSOITEMCRITERIACONDITION']._serialized_end=1291
  _globals['_CSOITEMCRITERIA']._serialized_start=1294
  _globals['_CSOITEMCRITERIA']._serialized_end=1604
  _globals['_CSOITEMRECIPE']._serialized_start=1607
  _globals['_CSOITEMRECIPE']._serialized_end=2086
  _globals['_CMSGDEVNEWITEMREQUEST']._serialized_start=2088
  _globals['_CMSGDEVNEWITEMREQUEST']._serialized_end=2170
  _globals['_CMSGINCREMENTKILLCOUNTATTRIBUTE']._serialized_start=2173
  _globals['_CMSGINCREMENTKILLCOUNTATTRIBUTE']._serialized_end=2313
  _globals['_CMSGAPPLYSTICKER']._serialized_start=2316
  _globals['_CMSGAPPLYSTICKER']._serialized_end=2450
  _globals['_CMSGMODIFYITEMATTRIBUTE']._serialized_start=2452
  _globals['_CMSGMODIFYITEMATTRIBUTE']._serialized_end=2535
  _globals['_CMSGAPPLYSTATTRAKSWAP']._serialized_start=2537
  _globals['_CMSGAPPLYSTATTRAKSWAP']._serialized_end=2630
  _globals['_CMSGAPPLYSTRANGEPART']._serialized_start=2632
  _globals['_CMSGAPPLYSTRANGEPART']._serialized_end=2706
  _globals['_CMSGAPPLYPENNANTUPGRADE']._serialized_start=2708
  _globals['_CMSGAPPLYPENNANTUPGRADE']._serialized_end=2783
  _globals['_CMSGAPPLYEGGESSENCE']._serialized_start=2785
  _globals['_CMSGAPPLYEGGESSENCE']._serialized_end=2852
  _globals['_CSOECONITEMATTRIBUTE']._serialized_start=2854
  _globals['_CSOECONITEMATTRIBUTE']._serialized_end=2931
  _globals['_CSOECONITEMEQUIPPED']._serialized_start=2933
  _globals['_CSOECONITEMEQUIPPED']._serialized_end=2991
  _globals['_CSOECONITEM']._serialized_start=2994
  _globals['_CSOECONITEM']._serialized_end=3424
  _globals['_CMSGADJUSTITEMEQUIPPEDSTATE']._serialized_start=3426
  _globals['_CMSGADJUSTITEMEQUIPPEDSTATE']._serialized_end=3523
  _globals['_CMSGADJUSTITEMEQUIPPEDSTATEMULTI']._serialized_start=3525
  _globals['_CMSGADJUSTITEMEQUIPPEDSTATEMULTI']._serialized_end=3619
  _globals['_CMSGSORTITEMS']._serialized_start=3621
  _globals['_CMSGSORTITEMS']._serialized_end=3655
  _globals['_CSOECONCLAIMCODE']._serialized_start=3657
  _globals['_CSOECONCLAIMCODE']._serialized_end=3751
  _globals['_CMSGSTOREGETUSERDATA']._serialized_start=3753
  _globals['_CMSGSTOREGETUSERDATA']._serialized_end=3822
  _globals['_CMSGSTOREGETUSERDATARESPONSE']._serialized_start=3825
  _globals['_CMSGSTOREGETUSERDATARESPONSE']._serialized_end=3978
  _globals['_CMSGUPDATEITEMSCHEMA']._serialized_start=3981
  _globals['_CMSGUPDATEITEMSCHEMA']._serialized_end=4115
  _globals['_CMSGGCERROR']._serialized_start=4117
  _globals['_CMSGGCERROR']._serialized_end=4150
  _globals['_CMSGREQUESTINVENTORYREFRESH']._serialized_start=4152
  _globals['_CMSGREQUESTINVENTORYREFRESH']._serialized_end=4181
  _globals['_CMSGCONVARVALUE']._serialized_start=4183
  _globals['_CMSGCONVARVALUE']._serialized_end=4229
  _globals['_CMSGREPLICATECONVARS']._serialized_start=4231
  _globals['_CMSGREPLICATECONVARS']._serialized_end=4293
  _globals['_CMSGUSEITEM']._serialized_start=4296
  _globals['_CMSGUSEITEM']._serialized_end=4438
  _globals['_CMSGREPLAYUPLOADEDTOYOUTUBE']._serialized_start=4440
  _globals['_CMSGREPLAYUPLOADEDTOYOUTUBE']._serialized_end=4540
  _globals['_CMSGCONSUMABLEEXHAUSTED']._serialized_start=4542
  _globals['_CMSGCONSUMABLEEXHAUSTED']._serialized_end=4588
  _globals['_CMSGITEMACKNOWLEDGED__DEPRECATED']._serialized_start=4591
  _globals['_CMSGITEMACKNOWLEDGED__DEPRECATED']._serialized_end=4749
  _globals['_CMSGSETITEMPOSITIONS']._serialized_start=4752
  _globals['_CMSGSETITEMPOSITIONS']._serialized_end=4914
  _globals['_CMSGSETITEMPOSITIONS_ITEMPOSITION']._serialized_start=4841
  _globals['_CMSGSETITEMPOSITIONS_ITEMPOSITION']._serialized_end=4914
  _globals['_CMSGGCREPORTABUSE']._serialized_start=4917
  _globals['_CMSGGCREPORTABUSE']._serialized_end=5101
  _globals['_CMSGGCREPORTABUSERESPONSE']._serialized_start=5103
  _globals['_CMSGGCREPORTABUSERESPONSE']._serialized_end=5194
  _globals['_CMSGGCNAMEITEMNOTIFICATION']._serialized_start=5196
  _globals['_CMSGGCNAMEITEMNOTIFICATION']._serialized_end=5298
  _globals['_CMSGGCCLIENTDISPLAYNOTIFICATION']._serialized_start=5301
  _globals['_CMSGGCCLIENTDISPLAYNOTIFICATION']._serialized_end=5483
  _globals['_CMSGGCSHOWITEMSPICKEDUP']._serialized_start=5485
  _globals['_CMSGGCSHOWITEMSPICKEDUP']._serialized_end=5534
  _globals['_CMSGGCINCREMENTKILLCOUNTRESPONSE']._serialized_start=5536
  _globals['_CMSGGCINCREMENTKILLCOUNTRESPONSE']._serialized_end=5660
  _globals['_CSOECONITEMDROPRATEBONUS']._serialized_start=5663
  _globals['_CSOECONITEMDROPRATEBONUS']._serialized_end=5806
  _globals['_CSOECONITEMLEAGUEVIEWPASS']._serialized_start=5808
  _globals['_CSOECONITEMLEAGUEVIEWPASS']._serialized_end=5920
  _globals['_CSOECONITEMEVENTTICKET']._serialized_start=5922
  _globals['_CSOECONITEMEVENTTICKET']._serialized_end=6001
  _globals['_CMSGGCITEMPREVIEWITEMBOUGHTNOTIFICATION']._serialized_start=6003
  _globals['_CMSGGCITEMPREVIEWITEMBOUGHTNOTIFICATION']._serialized_end=6068
  _globals['_CMSGGCSTOREPURCHASECANCEL']._serialized_start=6070
  _globals['_CMSGGCSTOREPURCHASECANCEL']._serialized_end=6113
  _globals['_CMSGGCSTOREPURCHASECANCELRESPONSE']._serialized_start=6115
  _globals['_CMSGGCSTOREPURCHASECANCELRESPONSE']._serialized_end=6166
  _globals['_CMSGGCSTOREPURCHASEFINALIZE']._serialized_start=6168
  _globals['_CMSGGCSTOREPURCHASEFINALIZE']._serialized_end=6213
  _globals['_CMSGGCSTOREPURCHASEFINALIZERESPONSE']._serialized_start=6215
  _globals['_CMSGGCSTOREPURCHASEFINALIZERESPONSE']._serialized_end=6286
  _globals['_CMSGGCBANNEDWORDLISTREQUEST']._serialized_start=6288
  _globals['_CMSGGCBANNEDWORDLISTREQUEST']._serialized_end=6361
  _globals['_CMSGGCREQUESTANNOUNCEMENTS']._serialized_start=6363
  _globals['_CMSGGCREQUESTANNOUNCEMENTS']._serialized_end=6391
  _globals['_CMSGGCREQUESTANNOUNCEMENTSRESPONSE']._serialized_start=6394
  _globals['_CMSGGCREQUESTANNOUNCEMENTSRESPONSE']._serialized_end=6524
  _globals['_CMSGGCBANNEDWORD']._serialized_start=6526
  _globals['_CMSGGCBANNEDWORD']._serialized_end=6648
  _globals['_CMSGGCBANNEDWORDLISTRESPONSE']._serialized_start=6650
  _globals['_CMSGGCBANNEDWORDLISTRESPONSE']._serialized_end=6750
  _globals['_CMSGGCTOGCBANNEDWORDLISTBROADCAST']._serialized_start=6752
  _globals['_CMSGGCTOGCBANNEDWORDLISTBROADCAST']._serialized_end=6842
  _globals['_CMSGGCTOGCBANNEDWORDLISTUPDATED']._serialized_start=6844
  _globals['_CMSGGCTOGCBANNEDWORDLISTUPDATED']._serialized_end=6895
  _globals['_CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT']._serialized_start=6898
  _globals['_CSOECONDEFAULTEQUIPPEDDEFINITIONINSTANCECLIENT']._serialized_end=7044
  _globals['_CMSGGCTOGCDIRTYSDOCACHE']._serialized_start=7046
  _globals['_CMSGGCTOGCDIRTYSDOCACHE']._serialized_end=7109
  _globals['_CMSGGCTOGCDIRTYMULTIPLESDOCACHE']._serialized_start=7111
  _globals['_CMSGGCTOGCDIRTYMULTIPLESDOCACHE']._serialized_end=7182
  _globals['_CMSGGCCOLLECTITEM']._serialized_start=7184
  _globals['_CMSGGCCOLLECTITEM']._serialized_end=7256
  _globals['_CMSGSDONOMEMCACHED']._serialized_start=7258
  _globals['_CMSGSDONOMEMCACHED']._serialized_end=7278
  _globals['_CMSGGCTOGCUPDATESQLKEYVALUE']._serialized_start=7280
  _globals['_CMSGGCTOGCUPDATESQLKEYVALUE']._serialized_end=7327
  _globals['_CMSGGCTOGCISTRUSTEDSERVER']._serialized_start=7329
  _globals['_CMSGGCTOGCISTRUSTEDSERVER']._serialized_end=7374
  _globals['_CMSGGCTOGCISTRUSTEDSERVERRESPONSE']._serialized_start=7376
  _globals['_CMSGGCTOGCISTRUSTEDSERVERRESPONSE']._serialized_end=7431
  _globals['_CMSGGCTOGCBROADCASTCONSOLECOMMAND']._serialized_start=7433
  _globals['_CMSGGCTOGCBROADCASTCONSOLECOMMAND']._serialized_end=7489
  _globals['_CMSGGCSERVERVERSIONUPDATED']._serialized_start=7491
  _globals['_CMSGGCSERVERVERSIONUPDATED']._serialized_end=7543
  _globals['_CMSGGCCLIENTVERSIONUPDATED']._serialized_start=7545
  _globals['_CMSGGCCLIENTVERSIONUPDATED']._serialized_end=7597
  _globals['_CMSGGCTOGCWEBAPIACCOUNTCHANGED']._serialized_start=7599
  _globals['_CMSGGCTOGCWEBAPIACCOUNTCHANGED']._serialized_end=7631
  _globals['_CMSGGCTOGCREQUESTPASSPORTITEMGRANT']._serialized_start=7633
  _globals['_CMSGGCTOGCREQUESTPASSPORTITEMGRANT']._serialized_end=7727
  _globals['_CMSGGAMESERVERINFO']._serialized_start=7730
  _globals['_CMSGGAMESERVERINFO']._serialized_end=8351
  _globals['_CMSGGAMESERVERINFO_SERVERTYPE']._serialized_start=8301
  _globals['_CMSGGAMESERVERINFO_SERVERTYPE']._serialized_end=8351
# @@protoc_insertion_point(module_scope)
