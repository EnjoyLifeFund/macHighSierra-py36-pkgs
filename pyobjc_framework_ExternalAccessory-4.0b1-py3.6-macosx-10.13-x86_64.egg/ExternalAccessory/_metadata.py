# This file is generated by objective.metadata
#
# Last update: Sun Jul  2 20:58:25 2017

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$EAAccessoryDidConnectNotification$EAAccessoryDidDisconnectNotification$EAAccessoryKey$EAAccessorySelectedKey$EABluetoothAccessoryPickerErrorDomain$'''
enums = '''$EABluetoothAccessoryPickerAlreadyConnected@0$EABluetoothAccessoryPickerResultCancelled@2$EABluetoothAccessoryPickerResultFailed@3$EABluetoothAccessoryPickerResultNotFound@1$EAConnectionIDNone@0$EAWiFiUnconfiguredAccessoryBrowserStateConfiguring@3$EAWiFiUnconfiguredAccessoryBrowserStateSearching@2$EAWiFiUnconfiguredAccessoryBrowserStateStopped@1$EAWiFiUnconfiguredAccessoryBrowserStateWiFiUnavailable@0$EAWiFiUnconfiguredAccessoryConfigurationStatusFailed@2$EAWiFiUnconfiguredAccessoryConfigurationStatusSuccess@0$EAWiFiUnconfiguredAccessoryConfigurationStatusUserCancelledConfiguration@1$EAWiFiUnconfiguredAccessoryPropertySupportsAirPlay@1$EAWiFiUnconfiguredAccessoryPropertySupportsAirPrint@2$EAWiFiUnconfiguredAccessoryPropertySupportsHomeKit@4$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'EAAccessory', b'isConnected', {'retval': {'type': 'Z'}})
    r(b'EAAccessory', b'setConnected:', {'arguments': {2: {'type': 'Z'}}})
    r(b'EAAccessoryManager', b'showBluetoothAccessoryPickerWithNameFilter:completion:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
