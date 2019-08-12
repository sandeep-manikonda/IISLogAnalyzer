import csv
import os


class Writer:
    def __init__(self, encoding, helpers):
        self.encoding = encoding
        self.helpers = helpers

    def write_ip(self):
        print("\t :: Writing csv for ip statistics")
        with open(os.getcwd() + "/reports/IpHits.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['IP', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'IP': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerIP.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_browser(self):
        print("\t :: Writing csv for browser statistics")
        with open(os.getcwd() + "/reports/Browser.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Browser', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Browser': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerBrowser.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_days(self):
        print("\t :: Writing csv for daily use")
        with open(os.getcwd() + "/reports/HitsPerDay.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Day', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Day': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerDay.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_endpoint(self):
        print("\t :: Writing csv for endpoint analyses")
        with open(os.getcwd() + "/reports/HitsPerEndpoint.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Endpunkt', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Endpunkt': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerEndpoint.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_hour(self):
        print("\t :: Writing csv for per hour report")
        with open(os.getcwd() + "/reports/HitsPerHour.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Stunde', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Stunde': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerHour.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_month(self):
        print("\t :: Writing csv for monthly results")
        with open(os.getcwd() + "/reports/HitsPerMonth.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Monat', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Monat': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerMonth.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_http_codes(self):
        print("\t :: Writing csv for http codes")
        with open(os.getcwd() + "/reports/HttpCodeHits.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['HTTP Code', 'Anzahl']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'HTTP Code': parts[0], 'Anzahl': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerHTTPCode.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_os(self):
        print("\t :: Writing csv for OS hits")
        with open(os.getcwd() + "/reports/OS.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_out_unknown = []
        csv_columns = ['OS', 'Hits']
        csv_columns_unknown = ['Unknown OS', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            if not entry.startswith('\t'):
                csv_out.append({'OS': parts[0], 'Hits': parts[1].replace('\n', '')})
            else:
                csv_out_unknown.append({'Unknown OS': parts[1], 'Hits': parts[2].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HitsPerOS.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns_unknown)
            writer.writeheader()
            writer.writerows(csv_out_unknown)

    def write_http_206(self):
        print("\t :: Writing csv for http codes")
        with open(os.getcwd() + "/reports/HTTPCode206.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Monat', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            if not entry.startswith('\t'):
                csv_out.append({'Monat': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/HTTP206HitsPerMonth.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_usage_month(self):
        print("\t :: Writing csv for usage per month")
        with open(os.getcwd() + "/reports/UsersPerMonth.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Monat', 'Benutzungen']
        for entry in data:
            parts = entry.split('\t')
            if not entry.startswith('\t'):
                csv_out.append({'Monat': parts[0], 'Benutzungen': parts[1].replace('\n', '')})
        with open(os.getcwd() + "/csvs/UsagesPerMonth.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def run_all(self):
        self.helpers.clean_up_csv()
        print(":: Converting reports to CSV files")
        self.write_ip()
        self.write_browser()
        self.write_days()
        self.write_endpoint()
        self.write_hour()
        self.write_month()
        self.write_http_codes()
        self.write_os()
        self.write_http_206()
        self.write_usage_month()
