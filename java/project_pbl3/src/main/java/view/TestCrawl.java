package view;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

public class TestCrawl {
	private static final String url = "https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu";
	
	public static void main(String[] args) {
		try {
			Document doc = Jsoup.connect(url).get();
			Elements elements = doc.select("div.container");
			
			System.out.println(elements.select("div.flex-1").size());
			
			
		} catch (IOException e) {
 			e.printStackTrace();
		} 
		
	}
}
