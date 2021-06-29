#import "Tweak.h"

%group CustomStatusBar

%hook _UIStatusBarStringView

-(void)setText:(id)arg1 {
	%orig(arg1);

	if ([arg1 isKindOfClass:[NSString class]] && ![arg1 containsString:@"%"] && ![arg1 containsString:@":"] && Enabled == YES) {
		NSLog(@"Found: %@", arg1);
		%orig(YTStatusLabel);
	}
}

%end /* end hook */

%end /* end group */

static void loadPrefs() {
	NSMutableDictionary *settings = [[NSMutableDictionary alloc] initWithContentsOfFile:@"/var/mobile/Library/Preferences/com.soup.ytservicechanger.plist"];

	NSLog(@"Exists = %i",[settings objectForKey:@"kEnabled"] ? [[settings objectForKey:@"kEnabled"] boolValue] : NO);

	if ([settings objectForKey:@"kEnabled"] ? [[settings objectForKey:@"kEnabled"] boolValue] : NO) {

		YTStatusLabel = [settings objectForKey:@"kStatusBarLabel"];
		Enabled = [[settings objectForKey:@"kEnabled"] boolValue];

		%init(CustomStatusBar)
	}
}

%ctor {
    loadPrefs();
    CFNotificationCenterAddObserver(CFNotificationCenterGetDarwinNotifyCenter(), NULL, (CFNotificationCallback)loadPrefs, CFSTR("bundleID/saved"), NULL, CFNotificationSuspensionBehaviorCoalesce);

}