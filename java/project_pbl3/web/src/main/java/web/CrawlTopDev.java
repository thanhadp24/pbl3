package web;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import java.util.ArrayList;

import java.io.IOException;

public class CrawlTopDev {

	public static void main(String[] args) throws IOException {
		String link = "https://topdev.vn/viec-lam-it/java-kt21?src=topdev.vn&medium=mainmenu";
		Document doc = Jsoup.connect(link).get();
		
		ArrayList<String> Job = new ArrayList<>();	
		ArrayList<String> Company = new ArrayList<>();
		ArrayList<String> Location = new ArrayList<>();
		ArrayList<String> Level = new ArrayList<>();
		ArrayList<String> Time = new ArrayList<>();

		for (int i = 0; i < 15; i++) {
			Element job = doc.select("div[class=flex-1]").get(i);
			// System.out.println(job);
			
			// h3 class="line-clamp-1"
			String tmp = job.selectFirst("h3.line-clamp-1 a").text();
			// System.out.println(tmp);
			Job.add(tmp);

			// div class="mt-1 line-clamp-1"
			String company = job.selectFirst("div.mt-1.line-clamp-1 a").text();
			// System.out.println(company);
			Company.add(company);

			String location = job.selectFirst("div.flex.flex-wrap.items-end.gap-2 > p:first-child").text();
			// System.out.println(location);
			Location.add(location);

			String level = job.selectFirst("div.flex.items-center.justify-start.gap-5").text();
			Level.add(level);
			

			String time = job.selectFirst("div.mt-4.flex.items-center.justify-between > p").text();
			Time.add(time);

		}

		for (int i = 0; i < Job.size(); i++) {
			System.out.println(Job.get(i) + ", " + Company.get(i) + ", " + Location.get(i) + ", " + Level.get(i) + ", "
					+ Time.get(i));
		}
	}

}