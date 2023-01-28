export const MIN_VALUE: number = 5;
export const MAX_VALUE: number = 1000;

export const CHART_SETUP = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            animation: false
        }
    },
    xAxis: {
        type: 'time',
        splitLine: {
            show: false
        }
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%'],
        splitLine: {
            show: false
        }
    },
    series: [{
        type: 'line',
        showSymbol: false,
        emphasis: {
            line: false,
        },
        data: []
    }]
};

export const CHART_THEME = {
    color: [
        '#53565A',
        '#F4D800'
    ]
};