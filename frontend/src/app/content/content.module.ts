import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CurrentPageComponent } from './current-page/current-page.component';
import { HelpPageComponent } from './help-page/help-page.component';
import { StatisticPageComponent } from './statistic-page/statistic-page.component';



@NgModule({
  declarations: [
    CurrentPageComponent,
    HelpPageComponent,
    StatisticPageComponent
  ],
  imports: [
    CommonModule
  ]
})
export class ContentModule { }
