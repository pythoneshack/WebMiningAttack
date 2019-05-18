import sys
import pandas as pd
import geoip2.database
import os


# reg_ex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"


def apache_to_pd(logfile):
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    d = []
    for line in logfile:
        split_line = line.split()
        # if re.match(reg_ex, split_line[0]):
        split_line[3] = split_line[3].replace("[", "")
        split_line[3] = split_line[3].replace(":", " ", 1)
        try:
            response = reader.city(split_line[0])
            country = response.country.name
            print(country)
            latitude = response.location.latitude
            longitude = response.location.longitude
            d.append(
                (split_line[0], split_line[8], split_line[9], split_line[6],
                 split_line[3], latitude, longitude, country))
        except:
            d.append(
                (split_line[0], split_line[8], split_line[9], split_line[6],
                 split_line[3], "UNKNOWN", "UNKNOWN", "UNKNOWN"))
        print(d)
    df_out = pd.DataFrame(d, columns=['Host', 'Status', 'Data', 'Endpoint', 'Date', 'Latitude', 'Longitude', 'Country'])
    df_out.to_csv(r'dataNewH.csv')
    reader.close()


def apache_output(line):
    split_line = line.split()
    return {'remote_host': split_line[0],
            'apache_status': split_line[8],
            'data_transfer': split_line[9],
            'date': split_line[3]
            }


def final_report(logfile):
    for line in logfile:
        line_dict = apache_output(line)
        print(line_dict)


if __name__ == "__main__":
    try:
        infile = open("data/dataAgg", 'r')
    except IOError:
        print("You must specify a valid file to parse")
        print(__doc__)
        sys.exit(1)
    #log_report = final_report(infile)
    #filelist = os.listdir('data')
    #df = [apache_to_pd(file) for file in filelist]
    apache_to_pd(infile)
    # print (log_report)
    infile.close()
