import { Component } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { SettingsService } from './shared/services/settings.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  public theme$: BehaviorSubject<string> = this.settingsService.getTheme();

  constructor(
    private settingsService: SettingsService
  ){}

}
