OK so the code here is to find which prism grids returned by the cfarm google mercator table, would cause a failure in the daycent service.


So we have a list of all gridx_gridy pairs from the cfarm table.              FullGoogleMercatorTableReturn.csv
We have a list of all weather files that the daycent service has access to.

We need a list of all gridx_gridy pairs from the cfarm table such that the daycent service would not return a file for that pair.
(note daycent service returns the file pair which matches, or it looks in a circle of +/- 10 (i.e. x=10, y=15 could return a file at x=0, y=25) )