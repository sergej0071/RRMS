import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { EChartsOption } from 'echarts';
import { map, Observable } from 'rxjs';
import { IPackageEChartOption, IProbabilityApi } from 'src/app/shared/interfaces';
import { ParseApiService } from 'src/app/shared/services/parse-api.service';
import { MAX_VALUE, MIN_VALUE } from 'src/app/shared/setup-charts';

@Component({
  selector: 'app-analysis-page',
  templateUrl: './analysis-page.component.html',
  styleUrls: ['./analysis-page.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AnalysisPageComponent implements OnInit {

  public probability$!: Observable<IPackageEChartOption>;

  public valueControl: FormControl<number | null> = new FormControl<number>(MIN_VALUE);

  public minValue: number = MIN_VALUE;
  public maxValue: number = MAX_VALUE;

  constructor(
    public parseApiService: ParseApiService
  ) { }

  public ngOnInit(): void {
    this.reloadData()
  }

  public reloadData() {
    this.probability$ = this.parseApiService.getProbability(this.valueControl.value!).pipe(
      map((value: IProbabilityApi) => ({
        temperature: this.setChart(value.temperature.value, value.temperature.amount, 'bar', 'Temp', 'Amount'),
        pressure: this.setChart(value.pressure.value, value.pressure.amount, 'bar', 'Pressure', 'Amount'),
        humidity: this.setChart(value.humidity.value, value.humidity.amount, 'bar', 'Humidity', 'Amount')
      })));
  }

  private setChart(dataFirst: number[], dataSecond: number[], type: 'bar', xName: string, yName: string): EChartsOption {
    return {
      color: ['#F4D800'],
      tooltip: {},
      xAxis: {
        name: xName,
        data: dataFirst,
        silent: false,
        splitLine: { show: false, },
      },
      yAxis: { name: yName },
      series: [{
        type,
        data: dataSecond,
        animationDelay: (idx) => idx * 10,
      }],
      animationEasing: 'elasticOut',
    };
  }

}
