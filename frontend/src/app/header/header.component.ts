import { Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { SettingsService } from '../shared/services/settings.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {

  public theme$: BehaviorSubject<string> = this.settingsService.getTheme();

  constructor(public settingsService: SettingsService) {}

  ngOnInit(): void {}

  switchTheme() {
    this.settingsService.switchTheme();
  }
}
