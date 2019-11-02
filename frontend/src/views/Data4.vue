<template>
    <div class="home">
        <div id="most-popular-areas">

        </div>
    </div>
</template>

<script>
	/* eslint-disable */
	import G2 from "@antv/g2"
	import axios from "axios"
	import consts from "@/assets/consts"
	export default {
		name: "Data4",
		data () {
			return {
				chartData: null,
				chart: null
			}
		},
		methods: {
			drawPie() {
				let sum=0;
				let data2=[]
				for (let key in this.chartData) {
					if (!this.chartData.hasOwnProperty(key)) continue
					data2.push({
						item: key,
						//count: this.chartData[key][1],
						percent: this.chartData[key][1]
					})
				}
				this.chart = new G2.Chart({
					container: "most-popular-areas",
					forceFit: true,
					height: "800",
					animate: false
				})
				this.chart.source(data2, {
					percent: {
						formatter: function formatter(val) {
							val = val * 100 + '%';
							return val;
						}
					}
				})
				this.chart.coord('theta', {
					radius: 0.75,
					innerRadius: 0.6
				})
				this.chart.tooltip({
					showTitle: false,
					itemTpl: '<li><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}: {value}</li>'
				});
				// 辅助文本
				this.chart.guide().html({
					position: ['50%', '50%'],
					html: '<div style="color:#8c8c8c;font-size: 20px;text-align: center;width: 10em;">福州商圈<br><span style="color:#8c8c8c;font-size:20px">人气对比</span></div>',
					alignX: 'middle',
					alignY: 'middle'
				});
				/*let interval* = */this.chart.intervalStack().position('percent').color('item').label('percent', {

					formatter: function formatter(val, item) {
						return item.point.item + ': ' + val;
					}
				}).tooltip('item*percent', function(item, percent) {
					percent = percent * 100 + '%';
					return {
						name: item,
						value: percent
					};
				}).style({
					lineWidth: 1,
					stroke: '#fff'
				});
				//interval.setSelected(data2[0])
				this.chart.render();
			}
		},
		mounted() {
			axios.get(consts.apiBase+"data/4").then((response) => {
				this.chartData = response.data[0]
				this.drawPie()
			})

		}
	}

</script>

<style scoped>

</style>