import { EChartsOption } from "echarts";

export interface IArticle {
  header: string;
  content: string;
}

export interface ICurrentValues {
  temperature: number;
  pressure: number;
  humidity: number;
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