#import "Tweak.h"

NSString* statusLabel;
BOOL enabled; /* Global variables moved to .x */

static NSString *const kHBCBPreferencesEnabledKey = @"Enabled";
static NSString *const kHBCBPreferencesStatusLabelKey = @"StatusLabel";
static NSString *const kHBCBPreferencesDomain = @"com.soup.ytservicechanger";

HBPreferences *preferences;

%group CustomStatusBar

%hook _UIStatusBarStringView

-(void)setText:(id)arg1 {
	if ([arg1 isKindOfClass:[NSString class]] && ![arg1 containsString:@"%"] && ![arg1 containsString:@":"]) {
		NSLog(@"Found: %@", arg1);

		return %orig(statusLabel);
	}
	else {
		%orig(arg1);
	}
}

%end /* end hook */

%end /* end group */

static void loadPrefs() {
	preferences = [[HBPreferences alloc] initWithIdentifier:kHBCBPreferencesDomain];

	[preferences registerBool:&enabled default:YES forKey:kHBCBPreferencesEnabledKey];
	[preferences registerObject:&statusLabel default:@"Default" forKey:kHBCBPreferencesStatusLabelKey];

	//NSLog(@"Exists = %i",[settings objectForKey:@"kEnabled"] ? [[settings objectForKey:@"kEnabled"] boolValue] : NO);

	//if ([settings objectForKey:@"kEnabled"] ? [[settings objectForKey:@"kEnabled"] boolValue] : NO) {
	//	StatusLabel = [settings objectForKey:@"kStatusBarLabel"];
	//}
}

%ctor {
    loadPrefs();
	%init(CustomStatusBar) /* Moved %init to the constructor, prevents it executing multiple times*/
}


