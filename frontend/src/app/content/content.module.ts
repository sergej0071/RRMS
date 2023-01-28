import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CurrentPageComponent } from './current-page/current-page.component';
import { HelpPageComponent } from './help-page/help-page.component';
import { StatisticPageComponent } from './statistic-page/statistic-page.component';
import { MatSliderModule } from '@angular/material/slider';



@NgModule({
  declarations: [
    CurrentPageComponent,
    HelpPageComponent,
    StatisticPageComponent
  ],
  imports: [
    CommonModule,
    MatSliderModule
  ]
})
export class ContentModule { }
