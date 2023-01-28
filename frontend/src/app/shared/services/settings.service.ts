import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { TranslateService } from '@ngx-translate/core';

@Injectable({
  providedIn: 'root',
})
export class SettingsService {

  private theme$: BehaviorSubject<string> = new BehaviorSubject('light');

  constructor(private translateService: TranslateService) {
    this.translateService.setDefaultLang('en');
  }

  public switchTheme() {
    this.theme$.next(this.theme$.getValue() === 'light' ? 'dark' : 'light');
  }

  public switchLang(lang: string) {
    if (lang === 'en' || lang === 'ru' || lang === 'ua') this.translateService.use(lang);
  }

  public getTheme(): BehaviorSubject<string> {
    return this.theme$;
  }
}
