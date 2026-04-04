package packet;

public class Code {
	public static String reverseWord(String word) {
		String reversed = "";
		for(int i = word.length() - 1; i >= 0; i--) {
			reversed += word.charAt(i);
		}
		return reversed;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String text = "Norvežanin Kjetil Jansrud osvojio je zlatnu"
						+ " medalju u superveleslalomu na Zimskim\n"
						+ "olimpijskim igrama u Sočiju pošto je za 30 stotih"
						+ " delova sekunde bio brži od\n"
						+ "drugoplasiranog Amerikanca Endrjua Vajbrehta.";
		String[] words = text.split(" ");
		for(String word: words) {
			System.out.println(reverseWord(word));
		}
	}

}
