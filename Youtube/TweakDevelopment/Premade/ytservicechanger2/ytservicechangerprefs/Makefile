
ARCHS = arm64 arm64e

include $(THEOS)/makefiles/common.mk

BUNDLE_NAME = YTServiceChangerPrefs

YTServiceChangerPrefs_FILES = SSCRootListController.m
YTServiceChangerPrefs_FRAMEWORKS = UIKit
YTServiceChangerPrefs_PRIVATE_FRAMEWORKS = Preferences
YTServiceChangerPrefs_INSTALL_PATH = /Library/PreferenceBundles
YTServiceChangerPrefs_CFLAGS = -fobjc-arc

include $(THEOS_MAKE_PATH)/bundle.mk

internal-stage::
	$(ECHO_NOTHING)mkdir -p $(THEOS_STAGING_DIR)/Library/PreferenceLoader/Preferences$(ECHO_END)
	$(ECHO_NOTHING)cp entry.plist $(THEOS_STAGING_DIR)/Library/PreferenceLoader/Preferences/$(BUNDLE_NAME).plist$(ECHO_END)

