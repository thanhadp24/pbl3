package web;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class Test {
	
	public static void main(String[] args) {
		String link = "https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu";
		try {
			Document doc = Jsoup.connect(link).get();
			int size = doc.select(".mt-4").select(".mb-4 last:mb-0").size();
			System.out.println(size);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		
	}
}
