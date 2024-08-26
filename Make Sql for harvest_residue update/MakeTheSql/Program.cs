// See https://aka.ms/new-console-template for more information
using CsvHelper;
using Microsoft.VisualBasic.FileIO;
using System.Globalization;
using System.Text.RegularExpressions;

using System;
using System.Reflection.PortableExecutable;
using CsvHelper.Configuration;

namespace Program
{
    public class DMRow
    {
        public string Crop { get; set; }
        public string DM_tonnes { get; set; }
        public string DM_sd { get; set; }
        public string HI_tonnes_yield_tonnes_biomass { get; set; }
        public string HI_sd { get; set; }

        public DMRow(dynamic inrow)
        {
            Crop = inrow.Crop.Replace(" ","");
            if (Crop.EndsWith('s'))
            {
                Crop = Crop.Remove(Crop.Length - 1);
            }
            DM_tonnes = inrow.DM_tonnes;
            DM_sd = inrow.DM_sd;
            HI_tonnes_yield_tonnes_biomass = inrow.HI_tonnes_yield_tonnes_biomass;
            HI_sd = inrow.HI_sd;


        }
    }

    public class DBRow
    {
        public string name { get; set; }
        public string crop_id { get; set; }
      
        public DBRow(dynamic inrow)
        {
            name = inrow.name.Replace(" ", "");
            if (name.EndsWith('s'))
            {
                name = name.Remove(name.Length - 1);
            }
            crop_id = inrow.crop_id;
           


        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            String csvFile = "D:\\CSU Repos\\CSU-python-scripting-cfarm-ntt\\Make Sql for harvest_residue update\\crop_hi_dm_rs_table.csv";
            string existingExport = "D:\\CSU Repos\\CSU-python-scripting-cfarm-ntt\\Make Sql for harvest_residue update\\out.csv";
         

            var CSVLines = new List<DMRow>();
            var DBlines = new List<DBRow>();

            using (var reader = new StreamReader(csvFile))
            using (var csv = new CsvReader(reader,CultureInfo.CurrentCulture))
            { 
                var records = csv.GetRecords<dynamic>();
                foreach (var row in records)
                {
                    //CSVLines.Add(row);
                    CSVLines.Add(new (row));
                }
            }

            using (var reader = new StreamReader(existingExport))
            using (var csv = new CsvReader(reader, CultureInfo.CurrentCulture))
            {
                var records = csv.GetRecords<dynamic>();
                foreach (var row in records)
                {
                    //CSVLines.Add(row);
                    DBlines.Add(new(row));
                }
            }

           var outLines = new List<(string,int)>();
            foreach(var line in CSVLines)
            {
                var matches = DBlines.Where(x => x.name.ToLower()==line.Crop.ToLower());
                foreach(var match in matches)
                {
                    outLines.Add(new($"update cfarm.harvest_residue set dm_mean={line.DM_tonnes},dm_sd={line.DM_sd}, harvest_index_mean={line.HI_tonnes_yield_tonnes_biomass},harvest_index_sd={line.HI_sd}  where crop_id = {match.crop_id};", Convert.ToInt16(match.crop_id)));


                }
                if (matches.Count() == 0)
                {
                    var a = line;
                }


            }
          var sorted= outLines.OrderBy(x => x.Item2).ToList();

            File.WriteAllLines("OutSqlharvestIndex.sql", sorted.Select(x=>x.Item1));

        }
    }
}