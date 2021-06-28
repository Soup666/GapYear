#import "Tweak.h"

%hook _UIStatusBarStringView

-(void)setText:(id)arg1 {
	%orig(arg1);
	if ([arg1 isKindOfClass:[NSString class]] && ![arg1 containsString:@"%"] && ![arg1 containsString:@":"]) {
		NSLog(@"Found: %@", arg1);

		return %orig(StatusLabel);
	}
}

%end /* end hook */