package seg;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

import test.Evaluator;
import test.Judge;

public class TrainModel {
	
	public static void main(String[] args) {
		String trainFile = "./data/train/train.txt";
		String modelFile = "./data/model/model.txt";
		getModel(trainFile, modelFile);
	}
	
	public static void getModel(String trainFile, String modelFile) {
		boolean train = true;
		int iterNum = 8;
		float totalTime = 0;
		if (train) {
			CWS cws = new CWS();

			for (int i = 0; i < iterNum; i++) {
				System.out.println("��"+ (i+1) + "�ε���...");
				Evaluator evaluator = new Evaluator();
				BufferedReader br;
				String line;				
				try {
					br = new BufferedReader( new InputStreamReader(
							new FileInputStream(trainFile), "utf-8"));
					while((line = br.readLine()) != null){
						ArrayList<Integer> y = new ArrayList<Integer>();
						if (line.isEmpty())
							continue;
						String x = loadExample(line.split("\t"), y);
						ArrayList<Integer> z = cws.decode(x);
						//System.out.println(z);
						evaluator.call(dumpExample(x, y), dumpExample(x, z));
						cws.weights.step += 1;
						if (!z.equals(y)) {
							cws.updateWeights(x, y, 1.0);  //������
							cws.updateWeights(x, z, -1.0);  //����ͷ�
						}
					}
					totalTime += evaluator.report();
					cws.weights.updateAll();
					cws.weights.average();
					cws.weights.unaverage();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			System.out.println("�������,��ʱ��: " + totalTime +"s" );
			cws.weights.saveModel(modelFile);
			System.out.println("����ģ�����");
		}
	}
	

	/**
	 * ���ִ��ǩ
	 * {B, M, E, S}
	 * ��ǩΪE��S���ֺ�Ϊ�ִʵ�
	 * @param words
	 * @param y
	 * @return
	 */
	public static String loadExample(String[] words, ArrayList<Integer> y) {
		String allWord = "";
		for (String word: words) {
			allWord += word;
			if (word.length() == 1)
				y.add(3);
			else {
				y.add(0);
				for (int i = 0; i < word.length()-2; i++) {
					y.add(1);
				}
				y.add(2);
			}
		}
		return allWord;
	}
	
	public static ArrayList<String> dumpExample(String x, ArrayList<Integer> y) {
		String cache = "";
		ArrayList<String> words = new ArrayList<String>();
		for (int i = 0; i < x.length(); i++) {
			cache += String.valueOf(x.charAt(i));
			if (y.get(i) == 2 || y.get(i) == 3) { //ΪE,S
				words.add(cache);
				cache = "";
			}
		}
		if (!cache.isEmpty()) {
			words.add(cache);
		}
		return words;
	}
	
}
