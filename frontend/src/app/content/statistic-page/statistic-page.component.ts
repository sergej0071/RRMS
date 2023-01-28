import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ThemeOption } from 'ngx-echarts';
import { BehaviorSubject, map, Observable, Subscription, timer } from 'rxjs';
import { IChartValue, IPackageEChartOption } from 'src/app/shared/interfaces';
import { CHART_SETUP, CHART_THEME, MAX_VALUE, MIN_VALUE } from 'src/app/shared/setup-charts';
import { BehaviorSubject, map, Observable, Subscription, switchMap, timer } from 'rxjs';
import { ILastValues, IPackageEChartOption } from 'src/app/shared/interfaces';
import { ParseApiService } from 'src/app/shared/services/parse-api.service';

@Component({
  selector: 'app-statistic-page',
  templateUrl: './statistic-page.component.html',
  styleUrls: ['./statistic-page.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StatisticPageComponent implements OnInit {

  public minValue: number = MIN_VALUE;
  public maxValue: number = MAX_VALUE;

  public valueControl: FormControl<number | null> = new FormControl<number>(MIN_VALUE);
  public value$: BehaviorSubject<number> = new BehaviorSubject<number>(MIN_VALUE);

  public subToValue!: Subscription;

  public chartTheme: ThemeOption = CHART_THEME;
  public options: any = CHART_SETUP;
  public updateOptions$!: Observable<IPackageEChartOption>;

  constructor(
    private parseApiService: ParseApiService
  ) { }

  ngOnInit(): void {
    this.subToValue = this.valueControl.valueChanges.subscribe(
      (newValue: number | null) => {
        if (!(newValue && +newValue && newValue >= MIN_VALUE)) this.valueControl.setValue(MIN_VALUE);
        else if (newValue > MAX_VALUE) this.valueControl.setValue(MAX_VALUE);
        else this.value$.next(newValue)
      }
    );

    this.updateOptions$ = timer(0, 1000).pipe(
      switchMap((): Observable<ILastValues> =>
        this.parseApiService.getLastValues(this.value$.getValue())),

      map((lastValues: ILastValues): IPackageEChartOption => ({
          temperature: { series: [{ data: lastValues.temperature }] },
          pressure: { series: [{ data: lastValues.pressure }] },
          humidity: { series: [{ data: lastValues.humidity }] }
        })
      ));
  }

  ngOnDestroy() {
    this.subToValue.unsubscribe();
  }
}
