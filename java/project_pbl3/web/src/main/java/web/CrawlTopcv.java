package web;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class CrawlTopcv {
	
	private static final String url = "https://www.topcv.vn/viec-lam";

	public static void main(String[] args) {
		
		try {
			Document page = Jsoup.connect(url).get();
			var elements = page.select("[class=row feature_job_item]");
			System.out.println(elements);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}
}
