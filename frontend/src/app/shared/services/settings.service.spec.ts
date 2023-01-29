import { BehaviorSubject, EMPTY } from "rxjs";
import { SettingsService } from "./settings.service";

describe('SettingService', () => {

    let settingsService: SettingsService;
    let theme$: BehaviorSubject<string>;

    beforeEach(() => {
        const spy = jasmine.createSpyObj('TranslateService', { setDefaultLang: undefined, use: EMPTY });
        settingsService = new SettingsService(spy);
        theme$ = settingsService.getTheme();
    });

    it('should default value be \'light\'', () => {
        expect(theme$.getValue()).toBe('light');
    })

    it('should switched theme', () => {
        expect(theme$.getValue()).toBe('light');
        settingsService.switchTheme();
        expect(theme$.getValue()).toBe('dark');
    })

});