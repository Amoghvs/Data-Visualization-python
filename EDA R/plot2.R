data<-read.table('household_power_consumption.txt',sep=";",header = TRUE,na.strings = "?")


data$Date <- as.Date(data$Date, format = "%d/%m/%Y")

# Subset the data
data <- subset(data, subset = (Date >= "2007-02-01" & Date <= "2007-02-02"))

# Convert dates and times
data$datetime <- strptime(paste(data$Date, data$Time), "%Y-%m-%d %H:%M:%S")

data$datetime <- as.POSIXct(data$datetime)

attach(data)
plot(Global_active_power ~ datetime,type="l",ylab = "Global Active Power (kilowatts)", xlab = "")
detach(data)


dev.copy(png, file = "plot2.png", height = 480, width = 480)
dev.off()
