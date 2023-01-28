import { EChartsOption } from "echarts";

export interface IArticle {
  header: string;
  content: string;
}

export interface IChartValue {
  value: [Date, number]
}

export interface ILastValues {
  temperature: IChartValue[];
  pressure: IChartValue[];
  humidity: IChartValue[];
}

export interface IPackageEChartOption {
  temperature: EChartsOption,
  pressure: EChartsOption,
  humidity: EChartsOption
}