# Anomaly-Detection-in-Network-Data
1. TestNetworkData.csv contains network data
2. Run "python timeseries_proto_dist_file_break.py"  to see timeseries . It will break the data into protocol wise parts.
3. Run the bash script "bash_scrp.sh" to determine time series of individual protocol
4. Run "python tcp_analyzer.py TCP.csv" to find out TCP specific details
5. Run "reset_analyzer.py RST.csv" to see reset specific details of data.
6. Note that TCP.csv is generated from step 2, RST.csv is generated from step 4
7. Pattern in anamoly and top targets sending RESET can be determined
