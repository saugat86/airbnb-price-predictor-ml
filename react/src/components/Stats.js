import { useState, useEffect } from "react";
import { Typography, Divider, Row, Col, Spin } from "antd";
import {
  ResponsiveContainer,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
} from "recharts";
import { getStats } from "../api/api";

const { Title } = Typography;
const COLORS = ["#0088FE", "#00b4c4", "#FFBB28", "#FF8042"];



const Stats = () => {
  const [statsData, setStatsData] = useState(null);

  useEffect(() => {
    getStats().then((data) => {
      setStatsData(data.stats);
    });
  }, []);

  return (
    <div>
      <Title>Athens' Airbnbs Stats</Title>
      <Divider />
      {statsData ? (
        <>
          <Row className="row" gutter={[24, 24]}>
            <Col sm={{ span: 24 }} lg={{ span: 12 }}>
              <div className="chart-container">
                <Title level={4}>Distance from Acropolis vs Price </Title>
                <div className="chart-inner">
                  <ResponsiveContainer>
                    <BarChart
                      data={statsData.bar_char_data_1}
                      margin={{
                        top: 5,
                        right: 30,
                        left: 20,
                        bottom: 5,
                      }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="Distance_from_Acropolis" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="avg_price" fill="#8884d8" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </Col>
            <Col sm={{ span: 24 }} lg={{ span: 12 }}>
              <div className="chart-container">
                <Title level={4}>Distance from Syntagma vs Price</Title>
                <div className="chart-inner">
                  <ResponsiveContainer>
                    <BarChart
                      data={statsData.bar_char_data_2}
                      margin={{
                        top: 5,
                        right: 30,
                        left: 20,
                        bottom: 5,
                      }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="distance_from_Syntagma" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="avg_price" fill="#82ca9d" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </Col>
          </Row>
          <Row className="row" gutter={[24, 24]}>
            <Col sm={{ span: 24 }} lg={{ span: 12 }}>
              <div className="chart-container">
                <Title level={4}>No of Airbnbs vs Price Range </Title>
                <div className="chart-inner">
                  <ResponsiveContainer>
                    <BarChart
                      data={statsData.histogram_data}
                      margin={{
                        top: 5,
                        right: 30,
                        left: 20,
                        bottom: 5,
                      }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="price_range" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="count" fill="#eb3464" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </Col>
            <Col sm={{ span: 24 }} lg={{ span: 12 }}>
              <div className="chart-container">
                <Title level={4}>Types of Rooms</Title>
                <div className="chart-inner">
                  <ResponsiveContainer>
                    <PieChart>
                      <Pie
                        data={statsData.pie_chart_data}
                        dataKey="count"
                        outerRadius={100}
                        label
                      >
                        {statsData.pie_chart_data.map((entry, index) => (
                          <Cell
                            key={`cell-${entry.room_type}`}
                            fill={COLORS[index % COLORS.length]}
                          />
                        ))}
                      </Pie>
                      <Legend
                      payload={
                        statsData.pie_chart_data.map(
                          (item, index) => ({
                            id: item.room_type,
                            type: "square",
                            value: `${item.room_type}`,
                            color: COLORS[index % COLORS.length]
                          })
                        )
                      }
                      />
                    </PieChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </Col>
          </Row>
          
          <Row className="row" gutter={[24, 24]}>
            <Col sm={{ span: 24 }} lg={{ span: 12 }}>
              <div className="chart-container">
                <Title level={4}>Average Price based on Accommodates </Title>
                <div className="chart-inner">
                  <ResponsiveContainer>
                    <BarChart
                      data={statsData.bar_char_data_3}
                      margin={{
                        top: 5,
                        right: 30,
                        left: 20,
                        bottom: 5,
                      }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="accommodates" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="avg_price" fill="#343538" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </Col>
            <Col sm={{ span: 24 }} lg={{ span: 12 }}>
              <div className="chart-container">
                <Title level={4}>Price based on number of reviews</Title>
                <div className="chart-inner">
                  <ResponsiveContainer>
                    <BarChart
                      data={statsData.bar_char_data_4}
                      margin={{
                        top: 5,
                        right: 30,
                        left: 20,
                        bottom: 5,
                      }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="reviews_per_month" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="avg_price" fill="#1aad9c" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </Col>
          </Row>
        
              <div className="chart-container">
                <Title level={4}>Average Price based on Area </Title>
                <div className="chart-inner">
                  <ResponsiveContainer>
                    <BarChart
                      data={statsData.bar_char_data_5}
                      margin={{
                        top: 5,
                        right: 30,
                        left: 20,
                        bottom: 5,
                      }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="area" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Bar dataKey="avg_price" fill="#59e31e" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
           
    
         
        </>
      ) : (
        <div className="stats-loader">
          <Spin size="large" />
        </div>
      )}
    </div>
  );
};

export default Stats;