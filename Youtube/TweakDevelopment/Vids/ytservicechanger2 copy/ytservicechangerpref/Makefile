
include $(THEOS)/makefiles/common.mk

BUNDLE_NAME = YTServiceChangerPref

YTServiceChangerPref_FILES = YTPRootListController.m
YTServiceChangerPref_FRAMEWORKS = UIKit
YTServiceChangerPref_PRIVATE_FRAMEWORKS = Preferences
YTServiceChangerPref_INSTALL_PATH = /Library/PreferenceBundles
YTServiceChangerPref_CFLAGS = -fobjc-arc

include $(THEOS_MAKE_PATH)/bundle.mk

internal-stage::
	$(ECHO_NOTHING)mkdir -p $(THEOS_STAGING_DIR)/Library/PreferenceLoader/Preferences$(ECHO_END)
	$(ECHO_NOTHING)cp entry.plist $(THEOS_STAGING_DIR)/Library/PreferenceLoader/Preferences/$(BUNDLE_NAME).plist$(ECHO_END)
