# Centime_APIAutomation

<html>
   <head>
     <h2>Test Cases</h2>
   </head>
	
   <body>
      <ul type = "disc">
         <li>Validate the Response of API of Stock Time Series for Dialy for Symbol IBM . - Expected output -Metadata should contain Symbol-IBM</li>
         <li>Validate the Response of API of Stock Time Series for Dialy for IBM for US Time Zone.- Expected output-Metadata should contain TimeZone -US/Eastern</li>
	 <li>Validate the Response of API of Stock Time Series with invalid function- Expected output -Error Message.</li>
         <li>Validate the Response of API of Stock Time Series for Dialy for current Date contains information of Open ,high,,low values -Expected output - Timeseries should contain values.</li>
	 <li>Validate the Response of API of Stock Time Series for Dialy for Empty Symbol.- Expected output-Error Message</li>   
      </ul>
   </body>
   <body>
	<h4>Command: pytest -v tests --html=report.html </h4>
	<h4>Alternate Command : pytesy -v -s tests</h4>
	<p>Reports will be genereated in report.html file in the Project Directory, logfile.log contains all the logs . Logging is written in such a way that it logs all the API URL , Payload ,Params,API Response codes,API Response</p>
	<p>requirements.txt contains all the dependencies</p>
	<p>Default html reporting is used . Allure Reporting can be integrated to get the better reports,Even fixtures can be used to mark the test cases</p>
	<p>Throttling is handled successfully only 5 API calls can be requested per minute if it exceeds it will wait and retry after a minute</p>

</body>
</html>
