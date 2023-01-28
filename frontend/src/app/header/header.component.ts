import { ChangeDetectionStrategy, Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { BehaviorSubject, Subscription } from 'rxjs';
import { SettingsService } from '../shared/services/settings.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class HeaderComponent implements OnInit, OnDestroy  {
  public theme$: BehaviorSubject<string> = this.settingsService.getTheme();
  public subToLangControl!: Subscription;
  public langControl: FormControl = new FormControl('en');

  constructor(public settingsService: SettingsService) {}

  ngOnInit(): void {
    this.subToLangControl = this.langControl.valueChanges.subscribe((value) =>
      this.settingsService.switchLang(value)
    );
  }

  ngOnDestroy(): void {
    this.subToLangControl.unsubscribe();
  }

  switchTheme() {
    this.settingsService.switchTheme();
  }
}
