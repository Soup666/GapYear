#import "Tweak.h"

NSString* statusLabel;
BOOL enabled;

HBPreferences *preferences;

%group CustomStatusBar

%hook _UIStatusBarStringView

-(void)setText:(id)arg1 {
	if ([arg1 isKindOfClass:[NSString class]] && ![arg1 containsString:@"%"] && ![arg1 containsString:@":"] && Enabled == YES) {
		NSLog(@"Found: %@", arg1);
		%orig(statusLabel);
	}
	else {
		%orig(arg1);
	}
}

%end /* end hook */

%end /* end group */

static void loadPrefs() {
	preferences = [[HBPreferences alloc] initWithIdentifier:@"com.soup.ytservicechanger"];

	[preferences registerBool:&enabled default:YES forKey:kEnabled];
	[preferences registerObject:&statusLabel default:@"Default" forKey:kStatusBarLabel];
}

%ctor {
    loadPrefs();
    %init(CustomStatusBar);
}