#include "SSCRootListController.h"

@implementation SSCRootListController

- (NSArray *)specifiers {
	if (!_specifiers) {
		_specifiers = [self loadSpecifiersFromPlistName:@"Root" target:self];
	}

	return _specifiers;
}

-(void)respring {
	[HBRespringController respring];
}

@end
